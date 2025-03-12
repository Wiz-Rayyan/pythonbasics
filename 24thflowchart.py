from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Add outer node
dot.node('Outer', 'Outer Node')

# Create a subgraph (cluster) that represents the inner node
with dot.subgraph('cluster_inner') as cluster:
    cluster.attr(label='Inner Node', style='filled', color='lightblue')  # Style for the inner node
    cluster.node('B', 'B')  # Node B
    cluster.node('D', 'D')  # Node D
    cluster.node('E', 'E')  # Node E

# Optionally, you can create edges to connect the outer node with the inner node cluster
dot.edge('Outer', 'cluster_inner')  # Connect outer node to the inner node cluster

# Render the graph (in this case, just print the source code)
print(dot.source)

# You can render the graph to a file using the following command:
dot.render('24th', format='png')  # This will save it as flowchart.png
