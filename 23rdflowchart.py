from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Add nodes for the flowchart
dot.node('A', 'A')
dot.node('B', 'B')
dot.node('C', 'C')
dot.node('D', 'D')
dot.node('E', 'E')
dot.node('F', 'F')
dot.node('G', 'G')
dot.node('h', ' h')

# Create edges based on the notation
dot.edge('A', 'B')
dot.edge('A', 'C')
dot.edge('B', 'D')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('D', 'F')
dot.edge('E', 'G')
dot.edge('F', 'G')

# Create a subgraph to cluster nodes B, D, E together
with dot.subgraph() as cluster:
    cluster.attr(rank='same')  # Optional: this keeps the nodes at the same level
    cluster.attr(label='Cluster')  # You can set a label for the cluster
    cluster.node('h', 'B')
    cluster.node('h', 'D')
    cluster.node('h', 'E')

# Render the graph (in this case, just print the source code)
print(dot.source)

# You can render the graph to a file using the following command:
dot.render('23rd', format='png')  # This will save it as flowchart.png
