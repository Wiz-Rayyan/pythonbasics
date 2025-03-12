from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Add nodes for the flowchart
dot.node('A', 'A')
dot.node('C', 'C')
dot.node('F', 'F')
dot.node('G', 'G')

# Create edges based on the notation
dot.edge('A', 'B')  # A to B
dot.edge('A', 'C')  # A to C
dot.edge('B', 'D')  # B to D
dot.edge('C', 'D')  # C to D
dot.edge('D', 'E')  # D to E
dot.edge('D', 'F')  # D to F
dot.edge('E', 'G')  # E to G
dot.edge('F', 'G')  # F to G

# Create a cluster (subgraph) that groups nodes B, D, E together as a single node
with dot.subgraph('cluster_BDE') as cluster:
    cluster.attr(label='||B, D, E||', style='rounded', color='lightgrey')  # Node label and styling
    cluster.node('B', 'B')  # Add B as a node
    cluster.node('D', 'D')  # Add D as a node
    cluster.node('E', 'E')  # Add E as a node

# Render the graph (in this case, just print the source code)
print(dot.source)

# You can render the graph to a file using the following command:
dot.render('22nd', format='png')  # This will save it as flowchart.png
