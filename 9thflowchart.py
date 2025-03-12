from graphviz import Digraph

# Create a new directed graph
G = Digraph()

# Set global node attributes
G.attr('node', fontname="Handlee")

# Set global edge attributes
G.attr('edge', fontname="Handlee")

# Define nodes
G.node('draw', 'Draw a picture')
G.node('win', 'You win!')
G.node('guess', 'Did they\nguess it?')
G.node('point', 'Point repeatedly\nto the same picture.')

# Define edges
G.edge('draw', 'guess')
G.edge('guess', 'win', label="Yes")
G.edge('point', 'guess')
G.edge('guess', 'point', label="No")

# Render and view the graph
G.render('game_decision', format='png', view=True)
