# Metrics

## Stress (stress)

This metric measures the stress of the layout. The stress is defined as the sum of squared differences between the Euclidean distances of the edges in the layout and the desired distances of the edges in the graph. The desired distance of an edge is the weight of the edge in the graph.

```math
\begin{equation}
\label{stress}
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