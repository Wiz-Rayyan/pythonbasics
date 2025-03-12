from graphviz import Digraph

# Create a new directed graph
G = Digraph()

# Set global node attributes
G.attr('node', fontname="Handlee", shape="ellipse", style="filled")

# Add outer node
G.node('Outer', 'Outer Node', fillcolor='lightgrey', pos='0,0!', width='2', height='2')

# Add middle node
G.node('Middle', 'Middle Node', fillcolor='lightblue', pos='0,0!', width='1.5', height='1.5')

# Add inner node
G.node('Inner', 'Inner Node', fillcolor='lightgreen', pos='0,0!', width='1', height='1')

# Optionally, you can connect the nodes if needed
G.edge('Outer', 'Middle', dir='none')  # No arrow for visual clarity
G.edge('Middle', 'Inner', dir='none')  # No arrow for visual clarity

# Render and view the graph
G.render('concentric_circles', format='png', view=True)

