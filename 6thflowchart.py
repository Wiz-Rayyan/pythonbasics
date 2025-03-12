import graphviz

dot = graphviz.Digraph(comment="islor")

# Corrected syntax for node attributes
dot.node('db1', 'isl hand gestures', color='aquamarine', style='filled')
dot.node('db2', 'isl facial features', color='aquamarine', style='filled')
dot.node('db3', 'isl other nmfs', color='aquamarine', style='filled')

# Correct database node with attributes
dot.node('b', 'database', shape='cylinder', style='filled')
dot.node('c', 'Processing', shape='box')

# Edges
for n in ['db1', 'db2', 'db3']:
    dot.edge(n, 'b')
dot.edge('b', 'c')

# Display the graph
dot.render('output', format='png', view=True)
