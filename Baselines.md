# Baseline Methods

## Circular layout (circo)

Graphviz documentation: https://graphviz.org/docs/layouts/circo/

The circular layout for graph drawing arranges the nodes (vertices) of a graph in a circle, with all nodes evenly spaced along the circumference. This layout style emphasizes the symmetry and regularity of a graph and is particularly useful for highlighting cyclical structures.

Edges in a circular layout can be drawn as straight lines or curved arcs that connect nodes. This layout is especially effective for visualizing graphs where each node has similar connectivity, such as in undirected cyclic graphs or networks with uniform interactions. It helps to minimize edge crossings when the graph is not too dense, making the structure clearer and easier to analyze visually.

Circular layouts are commonly used in social network analysis, computer network topology mapping, and bioinformatics, among other fields, where the relational patterns between elements are of interest.

See https://en.wikipedia.org/wiki/Circular_layout for details. 

## DeepGD (deepgd)

DeepGD (Deep Graph Drawing) is an advanced graph visualization method that leverages deep learning techniques to optimize the layout of complex networks. Unlike traditional force-directed methods that rely on iterative adjustments based on physical simulations, DeepGD uses neural network models trained on a dataset of graphs to learn the optimal placement of nodes directly. This approach aims to minimize traditional layout objectives such as edge crossings and node overlaps while ensuring that the layout visually reflects the inherent structure and properties of the graph.

The power of DeepGD lies in its ability to handle large and complex graphs more efficiently than traditional algorithms. By training on a diverse set of graph examples, the model learns to generalize well across different types of graphs, producing layouts that are not only aesthetically pleasing but also informative. This method adapts to various graph characteristics automatically, making it suitable for dynamic graphs where relationships and structures can change over time.

DeepGD is particularly useful in fields like data analytics, network security, and systems biology, where understanding the dynamic interactions and relationships within large data sets is crucial. Its ability to quickly generate clear and coherent visual representations from complex data makes it a valuable tool for researchers and analysts who require deep insights into networked information.

Paper link: https://arxiv.org/abs/2106.15347

## Layered graph drawing (dot)

Graphviz documentation: https://graphviz.org/docs/layouts/dot/

The "dot" layout is designed to display directed graphs with clear hierarchy and flow, organizing nodes into horizontal or vertical layers. Edges typically point in one direction—either downward or to the right—making it ideal for visualizing structures like organizational charts or data flow diagrams.

In practice, the layout minimizes edge crossings to enhance readability, involving the assignment of nodes to layers, optimizing node placement within those layers to reduce space, and aligning nodes across layers for a tidy appearance. Sophisticated algorithms help reorder nodes to further minimize crossings.

Widely used in areas like software engineering and project management, the dot layout is favored for its ability to clearly depict complex hierarchies and directional flows. It's especially valuable in visualizing class hierarchies in programming and task dependencies in project schedules, providing a straightforward and intuitive visual representation of complex information.

See https://en.wikipedia.org/wiki/Layered_graph_drawing for details.

## ForceAtlas2 (fa2)

ForceAtlas2 is a force-directed layout algorithm used primarily for large graph visualization, emphasizing the distribution of nodes in a way that reflects their relational properties. It operates based on physical simulations where nodes are treated as objects with repulsive forces (similar to charged particles), and edges act as springs holding these nodes together. The algorithm aims to position nodes in such a way that there is minimal overlapping and edges have uniform lengths, resulting in a graph that is aesthetically pleasing and easy to interpret.

The unique aspect of ForceAtlas2 is its adaptability to different graph structures. It includes adjustable settings such as gravity, which pulls nodes towards the center to avoid dispersion; scaling, which adjusts the relative importance of edge length; and strong gravity modes that can force a tighter layout. This makes ForceAtlas2 particularly effective for revealing clusters and community structures within networks, as well as maintaining a balance between attraction and repulsion among nodes to prevent the graph from becoming too sparse or too condensed.

ForceAtlas2 is extensively utilized in network analysis across various fields such as social science, biology, and computer science, where understanding the interconnectedness and the strength of relationships within data is crucial. Its ability to handle large networks efficiently while producing layouts that are both informative and visually engaging makes it a popular choice for researchers and analysts who require dynamic and insightful visualizations.

Paper link: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4051631/

## Force-directed Placement (fdp)

Graphviz documentation: https://graphviz.org/docs/layouts/fdp/

Force-directed placement, also known as force-directed graph drawing, is a popular and versatile algorithm used for visualizing graphs. It simulates a physical system where nodes are treated as electrically charged particles that repel each other, while edges act as springs that pull connected nodes together. The goal is to reach a state where the forces are balanced, resulting in a graph where nodes that are not connected are visually separated to reduce overlap, and edges are of more uniform length, enhancing the overall readability and aesthetics of the graph.

This algorithm is highly effective for revealing the underlying structure of a graph, such as clusters and patterns of connectivity, because it naturally separates densely connected node groups while highlighting looser associations. Adjustments can be made to the strength of the forces and the spring lengths to cater to specific visualization needs, allowing the algorithm to be fine-tuned for different types of data and scales of graphs.

Force-directed algorithms are widely used in various fields such as social network analysis, bioinformatics, and computer network architecture. They are particularly appreciated for their ability to create organic and aesthetically pleasing layouts of complex networks, making them intuitive to explore and analyze, especially when dealing with abstract or conceptual data structures.

See https://en.wikipedia.org/wiki/Force-directed_graph_drawing for details.

## Fast Multipole Multilevel Method (fmmm)

FMMM (Fast Multipole Multilevel Method) is a force-directed layout algorithm that efficiently computes node positions in large graphs by approximating the forces between nodes using the fast multipole method. It is designed to handle the challenges of visualizing complex networks with thousands or millions of nodes and edges, where traditional force-directed algorithms may become computationally expensive or slow.

The key advantage of FMMM is its ability to scale to large graphs while maintaining interactive performance, making it suitable for real-time graph visualization and exploration. By approximating the forces between nodes using a hierarchical multilevel approach, FMMM reduces the computational complexity of force calculations, allowing for efficient layout updates as the graph changes or evolves.

FMMM is commonly used in applications that require the visualization of massive networks, such as social networks, biological networks, and communication networks. Its speed and scalability make it a valuable tool for exploring and analyzing large-scale graphs, enabling users to interactively navigate and understand complex network structures.

## Graph Drawing via Gradient Descent (gd2)

The GD2 layout algorithm is a force-directed graph drawing method that optimizes the positions of nodes in a graph based on various aesthetic criteria. It uses a gradient descent approach to minimize an objective function that captures the desired layout properties, such as stress, edge crossings, and crossing angles. By iteratively updating node positions to reduce the objective function, gd2 produces visually appealing graph layouts that emphasize clarity and readability.

The GD2 algorithm is versatile and can be customized to optimize different combinations of aesthetic metrics, allowing users to tailor the layout to their specific visualization needs. It is particularly effective for visualizing small to medium-sized graphs with complex structures, as it balances the trade-offs between different layout criteria to create informative and aesthetically pleasing visualizations.

Paper link: https://arxiv.org/abs/2008.05584

We are providing the following variations for gd2 layouts:
- `gd2(metric=stress)`: Stress minimization 
- `gd2(metric=stress+xangle)`: Stress minimization + Crossing Angle minimization
- `gd2(metric=stress+xing)`: Stress minimization + Edge Crossing minimization
- `gd2(metric=xangle)`: Crossing Angle minimization
- `gd2(metric=xing)`: Edge Crossing minimization

## Kamada-Kawai (kk)

The Kamada-Kawai algorithm is a force-directed graph drawing method designed to produce visually appealing and interpretable layouts for undirected graphs. It treats the graph as a mechanical system, where nodes repel each other like charged particles, while edges act as springs that try to maintain a preferred length between connected nodes. The unique aspect of this algorithm is its definition of the ideal spring length, which is based on the shortest path distance between nodes in the graph. This method seeks to position nodes so that the geometric distances between them in the drawing closely match their graph-theoretic distances, minimizing a global energy function that measures the disparity between these distances.

This algorithm is particularly effective for graphs that are not too large, as it tends to emphasize an accurate and uniform representation of distances within the graph. This focus on maintaining a proportional and accurate distance makes the Kamada-Kawai layout especially suitable for graphs where the path length between nodes is an important characteristic, such as in social networks or molecular structures.

Due to its computational complexity, particularly for larger graphs, Kamada-Kawai is best applied where high accuracy in the depiction of relational distances is required and the graph size is manageable. It is widely used in applications where the clarity of the relationship between nodes (such as the closeness or farness) is crucial for the analysis, providing a clear, detailed, and spatially meaningful depiction of the network structure.

Paper link: http://itginsight.com/wp-content/uploads/2022/09/AN-ALGORITHM-FOR-DRAWING-GENERAL-UNDIRECTED-GRAPHSKadama-Kawai-layout.pdf

## Spring Model Layout (neato)

Graphviz documentation: https://graphviz.org/docs/layouts/neato/

Neato is a force-directed graph layout algorithm that optimizes the positions of nodes in a graph to minimize a global energy function. It treats the graph as a physical system where nodes repel each other like charged particles, while edges act as springs that pull connected nodes together. By iteratively adjusting node positions to reduce the energy function, Neato produces visually appealing layouts that emphasize clarity and readability.

The Neato algorithm is particularly effective for visualizing small to medium-sized graphs with complex structures, as it balances the trade-offs between different layout criteria to create informative and aesthetically pleasing visualizations. It is widely used in network analysis, social network visualization, and bioinformatics, where understanding the relationships and structures within the data is crucial.

Neato is well-suited for graphs that require an organic and aesthetically pleasing layout, as it produces clear and visually engaging representations of complex networks. Its ability to handle various graph structures and optimize layout properties makes it a valuable tool for researchers and analysts who need to explore and interpret graph data effectively.

See https://en.wikipedia.org/wiki/Spring_system for details.

## PivotMDS (pmds)

TODO

## Scalable Force-Directed Placement (sfdp)

Graphviz documentation: https://graphviz.org/docs/layouts/sfdp/

The SFDP (Scalable Force-Directed Placement) layout algorithm is a sophisticated graph drawing technique designed for large-scale graph visualization. It is based on the force-directed principle, which simulates a physical system where nodes repel each other like charged particles, and edges act as springs holding these nodes together. However, SFDP is particularly engineered to handle very large graphs efficiently, making it a go-to choice for handling complex datasets.

SFDP employs a multi-level technique that progressively refines the graph’s layout. It starts with a coarse representation of the graph to establish the basic structure and then gradually refines this layout by incorporating more details and adjusting node positions to minimize edge crossings and distribute nodes evenly. This approach significantly reduces the computational burden typically associated with force-directed algorithms, especially in the context of large graphs.

This algorithm is widely used in network analysis, especially where visualizing the structure and relationships in large networks is crucial. Fields such as social network analysis, web graph visualization, and bioinformatics benefit from SFDP’s ability to efficiently produce clear and informative visual representations of extensive data sets. Its ability to scale with graph size while maintaining an effective balance between performance and visual quality makes it a valuable tool in the arsenal of data analysts and researchers.

See https://en.wikipedia.org/wiki/Force-directed_graph_drawing for details.

## Multicriteria Scalable Graph Drawing via Stochastic Gradient Descent (sgd2)

The "Multicriteria Scalable Graph Drawing via Stochastic Gradient Descent" method is a graph drawing technique that utilizes stochastic gradient descent (SGD) to optimize the layout of large graphs based on multiple aesthetic criteria. This method addresses the challenge of creating graph visualizations that are not only scalable to very large datasets but also capable of optimizing for several layout properties simultaneously, such as minimizing edge crossings, achieving uniform edge lengths, and distributing nodes evenly across the drawing space.

SGD is employed to iteratively adjust the positions of nodes in a way that incrementally improves the overall layout according to the defined aesthetic criteria. By using stochastic updates, the algorithm efficiently handles large graphs by sampling and optimizing a subset of the graph's elements (nodes and edges) in each iteration, rather than requiring computations over the entire graph. This makes the process scalable and faster compared to methods that need full graph calculations in every step.

This approach is particularly useful in applications involving large networks where traditional graph drawing algorithms would struggle with computational complexity or fail to meet multiple aesthetic goals effectively. The ability to fine-tune the importance of different criteria and the flexibility of SGD allows for customized layouts that can adapt to specific needs of the visualization, such as clarity, structure highlighting, or aesthetic balance, making it a versatile tool for network analysts and data scientists dealing with complex and large-scale data structures.

Paper link: https://arxiv.org/abs/2112.01571

## SmartGD (smartgd)

SmartGD is a sophisticated graph drawing framework that leverages a Generative Adversarial Network (GAN) to generate straight-line graph layouts. Unlike traditional graph drawing methods that typically focus on optimizing a single aesthetic criterion, SmartGD is designed to optimize multiple aesthetic criteria simultaneously, even if these criteria are non-differentiable. This capability is significant because it allows for the optimization of graph layouts without the need to mathematically define or derive aesthetic metrics, which can be complex and time-consuming.

The core of SmartGD’s functionality is its ability to learn from high-quality layouts generated during its training phase. It uses a self-challenging mechanism to continuously improve its performance, adapting its strategy to optimize layouts according to a predefined importance of each aesthetic criterion. This method makes it particularly versatile and effective in handling diverse layout optimization challenges without relying on differentiable surrogate functions for non-differentiable criteria.

SmartGD has demonstrated its effectiveness and efficiency through extensive experimentation, showing good performance across various aesthetic criteria and combinations thereof. This performance is competitive with, and often surpasses, that of benchmark algorithms, making SmartGD a powerful tool for graph visualization in situations where multiple layout aesthetics are crucial.

Paper link: https://arxiv.org/abs/2206.06434

We are providing the following variations for SmartGD layouts:
- `smartgd(metric=human_preference)`: Human preference-based optimization
- `smartgd(metric=stress)`: Stress minimization
- `smartgd(metric=stress+xangle)`: Stress minimization + Crossing Angle minimization
- `smartgd(metric=stress+xing)`: Stress minimization + Edge Crossing minimization
- `smartgd(metric=xangle)`: Crossing Angle minimization
- `smartgd(metric=xing)`: Edge Crossing minimization

## Eigenvectors of Graph Laplacian (spectral)

The spectral layout is a graph drawing method that positions nodes using the eigenvectors of the graph's Laplacian matrix, which is derived from the difference between the diagonal matrix of node degrees and the adjacency matrix. This technique is rooted in spectral graph theory and uses particularly the second and third smallest eigenvectors to place nodes in a two-dimensional space. Such placement ensures that nodes with stronger or more direct connections are positioned closer together, effectively highlighting the graph's inherent clustering and community structure.

This layout is highly effective for visualizing structural properties of the graph, such as community clusters and connectivity, as it groups tightly connected nodes and separates less connected ones. The spectral layout is valuable in areas like social network analysis, biological network visualization, and any field where revealing natural groupings within the data is essential.

Using a principled mathematical approach, the spectral layout provides a clear, insightful view of complex networks, making it a preferred choice for applications requiring a deep understanding of network structures without iterative adjustments.

See https://en.wikipedia.org/wiki/Spectral_layout for details.

## Fruchterman-Reingold Force-directed Algorithm (spring)

The Fruchterman-Reingold algorithm is a force-directed method for graph drawing that aims to produce visually appealing diagrams by positioning nodes to maintain approximately equal edge lengths and minimize edge crossings. It treats nodes as charged particles that repel each other, while edges act like springs pulling connected nodes closer, creating a dynamic system that seeks a low-energy state with balanced forces.

In operation, the algorithm adjusts node positions iteratively, applying a cooling factor to gradually decrease the movement range (or "temperature") as iterations progress. This process helps stabilize the layout and prevent oscillations, ensuring nodes settle into a visually coherent configuration that reflects the underlying graph structure. The temperature mechanism is crucial for escaping local minima, allowing the layout to evolve toward a more optimal arrangement.

This algorithm is widely used for small to medium-sized graphs and is popular due to its simplicity and effectiveness in creating clear and understandable visualizations. It is particularly valuable in fields like social network analysis, where the relational dynamics between individuals or groups are central to the study. The Fruchterman-Reingold method provides a balance between aesthetic appeal and computational efficiency, making it a preferred choice for interactive graph visualization applications.

See https://en.wikipedia.org/wiki/Force-directed_graph_drawing for details.

## Radial Layout (twopi)

Graphviz documentation: https://graphviz.org/docs/layouts/twopi/

The radial layout is a graph drawing method where nodes are placed in concentric circles around a central point or root node, with the layout typically organized to emphasize hierarchical structures within the graph. This method is particularly effective for visualizing tree-like structures or networks with clear central nodes and peripheral layers of related nodes.

In a radial layout, nodes are arranged such that their radial position (distance from the center) and angular position (angle around the circle) depend on their hierarchical level and their relationship to other nodes. This creates a clear visual distinction between levels of hierarchy: nodes closer to the center are typically more central or significant within the network, while outer nodes represent peripheral or less connected entities.

This layout is commonly used in network visualizations where understanding the levels of influence or the flow of information is crucial, such as in organizational charts, network security diagrams, and family trees. The radial layout provides a compact and intuitive visualization, making it easier to observe relationships and hierarchies at a glance. It's particularly useful for displaying networks with a clear central authority or organized layers, facilitating a quick understanding of the overall structure and individual node relationships within the graph.

