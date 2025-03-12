from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Add nodes and edges for the flowchart A {B / C} -> D {E / F} -> G
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

# Render the graph (in this case, just print the source code)
print(dot.source)

# You can render the graph to a file using the following command:
dot.render('flowchart', format='png')  # This will save it as flowchart.png
