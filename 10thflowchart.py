from graphviz import Digraph

# Create a new directed graph
G = Digraph()

# Set global node attributes (font and shape)
G.attr('node', fontname="Handlee", shape="box", style="filled", color="lightblue", fillcolor="lightyellow")

# Define nodes with custom images (logos) and colors
G.node('draw', label="", image=r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-17 055727.png", labelloc="b", width="1.5", height="1.5", fixedsize="true")
G.node('win', label="You win!", fillcolor="lightgreen")
G.node('guess', label="Did they\nguess it?", fillcolor="pink")
G.node('point', label="", image=r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-17 061255.png", labelloc="b", width="1.5", height="1.5", fixedsize="true")

# Define edges with colors and labels
G.edge('draw', 'guess')
G.edge('guess', 'win', label="Yes", color="red")
G.edge('point', 'guess')
G.edge('guess', 'point', label="No", color="blue")

# Render and view the graph
G.render('output_graph', format='png', view=True)
