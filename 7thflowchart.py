
import graphviz
dot = graphviz.Digraph(comment='islor')
dot.attr(newrank='true') # aligning clustersw
input_style  = {'color': 'plum', 'style' : 'filled', 'fillcolor': 'lightsalmon'}
marker_style = {'shape': 'box', 'color': 'skyblue', 'style' : 'filled'}
meanhood_style = {'shape': 'box', 'color' : 'skyblue', 'style': 'filled'}
marker_cluster_style = {**marker_style, 'fillcolor': '#F2A48188'}
tis_style = {'shape': 'doubleoctagon', 'color':'mediumseagreen', 'style': 'filled'}
dot.node('sig', 'ISL Translation System', input_style)
dot.node('sag', 'Matrix Multiplication', input_style)
dot.node('geo', 'Text Conversion API', input_style)
dot.node('aux', 'CNN', input_style)
dot.node('mnhd', 'user-interface', meanhood_style)
# basic markers
markers= ['Application/Website', 'Support Vector Machines', 'Decision Trees and Random Forests', 'Hidden Markov Models ', 'Gesture to text mapping']
for idx, m in enumerate(markers): 
    dot.node(f'm{idx}', m, marker_style)
#counters
dot.node('mc0', 'Scale-Invariant Feature Transform', marker_style)
dot.node('mcl', 'Optical Flow', marker_style)
#similarity
dot.node('m51', 'webcam', marker_style)
dot.node('m52', 'takes video input')
dot.node('m53', 'frames processing', marker_style)             
#  distance
dot.node('m61', 'Algorithms & Techniques', marker_style)
dot.node('m62', 'Stochastic Gradient Descent')
dot.node('m63', 'Transfer Learning', marker_style)
dot.node('m64', 'K-Fold Cross Validation')
# crop
dot.node('m71', 'Data Augumentation', marker_style)
dot.node('m72', 'Background Subtraction')
dot.node('m73', 'Contour Detection', marker_style)

# dot.node('point', label="", image=r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-17 061255.png", labelloc="b", width="1.3", height="1", fixedsize="true", shape="none")
#pixel-mowing
dot.node('m8', 'Text Display Interface', marker_style)
#TLS
dot.node('tls', 'Data transript', tis_style)
dot.node('tls2', 'English/Hindi LiveTranslation', tis_style)       
       # define marker clusters
with dot.subgraph (name='cluster_mw') as c: 
    c.edges([('mo', 'mc0')]) 
    c.attr(label='.', **marker_cluster_style)
with dot.subgraph (name='cluster bs') as c: 
    c.edges ([('m1', 'mcl')]) 
    c.attr(label='ML', **marker_cluster_style)
with dot.subgraph (name='cluster_sim') as c: 
    c.edges ([('m51', 'm52'), ('m52', 'm53')])
    c.attr(label='', **marker_cluster_style)
with dot.subgraph (name='cluster dist') as c: 
    c.edges([('m61', 'm62'), ('m62', 'm63'), ('m63', 'm64')]) 
    c.attr(label='', **marker_cluster_style)
with dot.subgraph (name='cluster_crop') as c: 
    c.edges ([('m71', 'm72'), ('m72', 'm73')])
    c.attr(label='Accounting for slight variation', **marker_cluster_style)   
for m in ['mnhd', 'm0', 'm1', 'm2', 'm3', 'm4', 'm51', 'm61', 'm71']:
    dot.edge('sig', m)
# meanhood -> similarity
dot.edge('mnhd', 'm51')
# dot.edge( 'point','m61')
#input -> crop group
dot.edge('m2', 'm71')
dot.edge('m64', 'm71')
dot.edge('sag', 'm71')
dot.edge('aux', 'm71')
#aux connections
dot.edge('aux', 'm1')
dot.edge('aux', 'm2')
#geo -> pixel-mowing 
dot.edge('geo','m8')
dot.edge('m53','m71')
dot.edge('m3', 'tls', label='(model sequences of gestures \n and predict future states \n based on past observations) ')
dot.edge('sig', 'm3')
dot.edge('m73','Support Vector Machines', label='to identify the shape and position \n of the hand \n in the image.')
dot.edge('Support Vector Machines', 'tls')
dot.edge('m2', 'Post-Processing action', label=' for gesture classification tasks')
# TLS
for m in ['mc0', 'mcl', 'm2', 'NLP correction', 'Post-Processing action', 'Error Handling', 'm63', 'm73']:
    dot.edge(m, 'tls')
dot.edge('tls', 'm8')
#TLS2
for m in ['m1', 'mcl', 'm2', 'm3', 'm4', 'm53', 'm63', 'm73', 'm8']:
    dot.edge(m, 'tls2')













dot.render('7th', format='png', view=True)