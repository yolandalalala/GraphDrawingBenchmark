# Metrics

## Stress (stress)

This metric measures the stress of the layout. The stress is defined as the sum of squared differences between the Euclidean distances of the edges in the layout and the desired distances of the edges in the graph. The desired distance of an edge is the weight of the edge in the graph.

```math
\begin{equation}
L_\text{stress}=
\sum_{u, v \in V, u \neq v}
    w_{uv} \left(\|\mathbf{x}_u - \mathbf{x}_v\| - d_{uv}\right)^2 ,
\end{equation}
```

## Edge Crossing (xing)

This metric measures the number of edge crossings in the layout.

## Crossing Angle (xangle)

This metric measures the sum of crossing angles of the edges in the layout. The crossing angle of two edges is defined as the acute angle between the two edges at the crossing point.

```math
\begin{align}
L_\mathrm{xangle} &= \sum_{(\vec{u},\vec{v}) \in \mathrm{crossings(G)}} \left|\arcsin<\frac{\vec{u}}{\|\vec{u}\|},\frac{\vec{v}}{\|\vec{v}\|}>\right|
\end{align}
```

## Incident Angle (iangle)

This metric measures the sum of incident angles of the edges in the layout. The incident angle is defined as as the sharpest angles formed by incident edges over common vertices.

```math
\begin{align}
    L_\text{angle} = 
    \sum_{v \in V}
    \sum_{\theta_v^{(i)}\in \text{angles}(v)} \bigg|\frac{2\pi}{\deg(v)}-\theta_v^{(i)}\bigg|,
\end{align}
```

## Node Occlusion (ring)

This metric measures the degree of node clustering in a graph layout. The node occlusion is defined as the sum of the exponential distances between the nodes in the layout.

```math
\begin{align}
L_\text{node occlusion} =
\sum_{\substack{u,v \in V \\ u \neq v}}
e^{-\|\mathbf{x}_u - \mathbf{x}_v\|}.
\end{align}
```

## Edge Uniformity (absedge)

This metric measures the uniformity of the edge lengths in the layout. The edge uniformity is defined as the sum of the absolute differences between the edge lengths and the average edge length in the layout.

```math
\begin{align}
L_\text{edge} = 
    \frac{1}{|E|}
    \sum_{(u,v) \in E} \frac{(l_{uv} - \bar{l})^2}{\bar{l}^2},
\qquad \begin{cases}
    l_{uv} = \|\mathbf{x}_u - \mathbf{x}_v\|\\
    \bar{l} = 1\\
\end{cases}
\end{align}
```

## t-SNE Score (tsne)

This metric measures the discrepancy of node distances between the Euclidian layout space and the graph space using t-distributed stochastic neighbor embedding (t-SNE).

```math
\begin{align}
    L_\text{t-SNE} = \sum_{\substack{i,j\\i \neq j}} p_{ij}\log\frac{p_{ij}}{q_{ij}}.
    \label{equ:tsne-loss}
\end{align}
```
where
```
\begin{align}
    p_{ij} = p_{ji} &= \frac{p_{j|i}+p_{i|j}}{2N} \\ 
    p_{j|i} &= \frac{\exp(-\frac{d_{ij}^2}{2\sigma_i^2})}{\sum_{\substack{k\\k\neq i}}\exp(-\frac{d_{ik}^2}{2\sigma_i^2})} \\
    q_{ij} = q_{ji} &= \frac{(1+||\mathbf{x}_i-\mathbf{x}_j||^2)^{-1} }{\sum_{\substack{k,l\\k \neq l}}(1+||\mathbf{x}_k-\mathbf{x}_l||^2)^{-1}}
\end{align}
```

#  Relative Neighborhood Graph Jaccard Distance (rng)

This metric measures the similarity of the relative neighborhood graph (RNG) between the graph space and the layout space. The RNG Jaccard distance is defined as the Jaccard distance between the RNGs of the graph and the layout.
