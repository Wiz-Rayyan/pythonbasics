from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Set global node attributes
dot.attr('node', fontname="Handlee", shape="box", style="filled", color="lightblue", fillcolor="lightyellow")

# Define nodes
dot.node('A', 'A')
dot.node('B', 'B')
dot.node('C', 'C')
dot.node('D', 'D')
dot.node('Table1', 'Table1')
dot.node('Table2', 'Table2')
dot.node('Table3', 'Table3')
dot.node('Table4', 'Table4')
dot.node('E', 'E')
dot.node('F', 'F')
dot.node('G', 'G')
dot.node('H', 'H')
dot.node('J', 'J')
dot.node('J2', 'J2')

# Define edges
dot.edge('A', 'C')  # A -> C
dot.edge('D', 'Table1')  # D -> Table1
dot.edge('D', 'Table2')  # D -> Table2
dot.edge('D', 'Table3')  # D -> Table3
dot.edge('D', 'Table4')  # D -> Table4
dot.edge('E', 'Table3')  # E -> Table3
dot.edge('E', 'Table4')  # E -> Table4
dot.edge('B', 'H')  # B -> H
dot.edge('J', 'F')  # J -> F
dot.edge('J2', 'G')  # J2 -> G
dot.edge('F', 'H')  # F -> H
dot.edge('G', 'H')  # G -> H

# Define clusters for groupings
with dot.subgraph(name='cluster_D') as cluster:
    cluster.attr(label='D')
    cluster.node('Table1')
    cluster.node('Table2')
    cluster.node('Table3')
    cluster.node('Table4')

with dot.subgraph(name='cluster_E') as cluster:
    cluster.attr(label='E')
    cluster.node('Table3')
    cluster.node('Table4')

with dot.subgraph(name='cluster_B') as cluster:
    cluster.attr(label='B')
    cluster.node('F')
    cluster.node('G')

# Render and view the graph
dot.render('25th', format='png', view=True)

