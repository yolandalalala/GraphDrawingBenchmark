from smartgd.constants import DATASET_S3_BUCKET, DATASET_ROOT

import os
import re
import multiprocessing
from functools import wraps
from typing import Optional, Type

from tqdm.auto import tqdm
import botocore
import boto3
import torch_geometric as pyg


# TODO: use s3fs async instead of boto3
def s3_dataset_syncing(_cls: Optional[Type[pyg.data.Dataset]] = None, /, *,
                       bucket_name: str = DATASET_S3_BUCKET):

    class Decorator:

        def __init__(self, decorated: Type[pyg.data.Dataset]):
            self.decorated = decorated

        def __call__(self, *args,
                     download_from_s3=True,
                     upload_to_s3=False,
                     **kwargs) -> pyg.data.Dataset:

            original_download = self.decorated.download

            @wraps(original_download)
            def download(wrapped_self: pyg.data.Dataset):
                if not download_from_s3:
                    return original_download(wrapped_self)

                s3 = boto3.resource('s3')
                bucket = s3.Bucket(bucket_name)
                prefix = os.path.basename(wrapped_self.root) + "/"
                folder = bucket.Object(prefix)

                try:
                    folder.get()
                except botocore.exceptions.ClientError as e:
                    if e.response["Error"]["Code"] == "NoSuchKey":
                        print(f"S3 cache for {prefix} not found.")
                        return original_download(wrapped_self)
                    else:
                        raise e

                collection = bucket.objects.filter(Prefix=prefix)
                jobs = list(map(lambda obj: (bucket_name, obj.key, f"{DATASET_ROOT}/{obj.key}"), collection))
                pool = multiprocessing.Pool(multiprocessing.cpu_count() * 8, _initialize_s3_client)
                results_iter = pool.imap_unordered(_download_from_s3, jobs)

                for _ in tqdm(results_iter, total=len(jobs), desc="Download from S3"):
                    pass

                pool.close()
                pool.join()

                if not pyg.data.dataset.files_exist(wrapped_self.raw_paths):
                    return original_download(wrapped_self)

            def upload(wrapped_self: pyg.data.Dataset):
                if not pyg.data.dataset.files_exist(wrapped_self.raw_paths):
                    original_download(wrapped_self)
                if not pyg.data.dataset.files_exist(wrapped_self.processed_paths):
                    wrapped_self.process()

                s3 = boto3.resource('s3')
                bucket = s3.Bucket(bucket_name)
                prefix = os.path.basename(wrapped_self.root) + "/"
                bucket.put_object(Key=prefix)
                collection = os.walk(wrapped_self.root)

                def get_jobs():
                    for root, dirs, files in collection:
                        for file in files:
                            path = os.path.join(root, file)
                            yield bucket_name, re.sub(f"^{DATASET_ROOT}/", "", path), path

                jobs = list(get_jobs())
                pool = multiprocessing.Pool(multiprocessing.cpu_count() * 8, _initialize_s3_client)
                results_iter = pool.imap_unordered(_upload_to_s3, jobs)

                for _ in tqdm(results_iter, total=len(jobs), desc="Upload to S3"):
                    pass

                pool.close()
                pool.join()

            self.decorated.download = download
            self.decorated.upload = upload

            dataset = self.decorated(*args, **kwargs)

            if upload_to_s3:
                dataset.upload()

            return dataset

    if _cls:
        return s3_dataset_syncing()(_cls)
    return Decorator


_s3_client = None


def _initialize_s3_client():
    global _s3_client
    _s3_client = boto3.resource('s3')


def _download_from_s3(job):
    bucket, key, file = job
    os.makedirs(os.path.dirname(file), exist_ok=True)
    if not os.path.exists(file):
        _s3_client.Bucket(bucket).download_file(Key=key, Filename=file)


def _upload_to_s3(job):
    bucket, key, file = job
    _s3_client.Bucket(bucket).upload_file(Filename=file, Key=key)
