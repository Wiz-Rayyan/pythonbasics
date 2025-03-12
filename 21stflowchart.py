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

# Create edges based on the notation
dot.edge('A', 'B')
dot.edge('A', 'C')
dot.edge('B', 'D')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('D', 'F')
dot.edge('E', 'G')
dot.edge('F', 'G')

# Create a subgraph to cluster nodes B, D, E inside a box
with dot.subgraph() as cluster:
    cluster.attr(rank='same')  # Optional: keeps nodes at the same level
    cluster.attr(label='Cluster', style='rounded', color='lightgrey')  # Box styling
    cluster.node('B')
    cluster.node('D')
    cluster.node('E')

# Render the graph (in this case, just print the source code)
print(dot.source)

# You can render the graph to a file using the following command:
dot.render('21st', format='png')  # This will save it as flowchart.png
