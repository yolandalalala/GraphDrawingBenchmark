# Model artifact settings
CKPT_S3_BUCKET = "smartgd-checkpoints"
MODEL_S3_BUCKET = "smartgd-models"
ASSET_S3_BUCKET = "smartgd-predictions"
DYNAMODB_REGION = "us-east-1"
LAYOUTS_DB_PREFIX = "smartgd-layouts."
ALIAS_DB_NAME = "smartgd-layout-method-aliases"

# Dataset settings
DATASET_ROOT = "datasets"
DATASET_S3_BUCKET = "smartgd-datasets"

# AimStack settings
AIMSTACK_SERVER_URL = "smartgd.xiaoqiwang.net:53800"
AIMSTACK_UI_URL = "smartgd.xiaoqiwang.net:80/experiments"
AIMSTACK_S3_BUCKET = "smartgd-aim-repo"

# Experiment constants
TRAIN_PREFIX = "train_"
VAL_PREFIX = "val_"
TEST_PREFIX = "test_"

EPS = 1e-5
