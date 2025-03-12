from graphviz import Digraph

# Create a new directed graph
G = Digraph('G')

# Subgraph for Frontend Services (Website and Interface)
with G.subgraph(name='cluster_Frontend') as c:
    c.attr(label='Frontend Services')
    c.node('web_app', shape='Mrecord', label='{User Interface|React.js}')
    c.node('camera_input', shape='Mrecord', label='{Camera Input|Live Video Capture}')
    c.node('text_output', shape='Mrecord', label='{Text Output|Translated Text}')

# Subgraph for Backend Services (Core Processing)
with G.subgraph(name='cluster_Backend') as c:
    c.attr(label='Backend Processing')
    
    # Subgraph for Preprocessing
    with c.subgraph(name='cluster_Preprocessing') as preprocess:
        preprocess.attr(label='Preprocessing')
        preprocess.node('feature_extraction', shape='Mrecord', label='{Feature Extraction|OpenCV, Haar-like features}')
        preprocess.node('nmf_detection', shape='Mrecord', label='{NMF Detection|Facial Expressions, Head Movements}')
    
    # Subgraph for Machine Learning Models
    with c.subgraph(name='cluster_ML_Models') as ml_models:
        ml_models.attr(label='Machine Learning Models')
        ml_models.node('svm_model', shape='Mrecord', label='{Support Vector Machine|Classification, SVM equations}')
        ml_models.node('entropy_calc', shape='Mrecord', label='{Entropy Calculation|Minimizing Uncertainty}')
        
    # Subgraph for NLP Processing
    with c.subgraph(name='cluster_NLP') as nlp:
        nlp.attr(label='Natural Language Processing')
        nlp.node('language_processing', shape='Mrecord', label='{NLP|TensorFlow, PyTorch}')

# Subgraph for Database (Storage and Data Management)
with G.subgraph(name='cluster_Database') as c:
    c.attr(label='Database')
    c.node('isl_dataset', shape='Mrecord', label='{ISL Dataset|ISL gestures, NMFs}')
    c.node('text_database', shape='Mrecord', label='{Text Database|English/Hindi Phrases}')

# Define edges between nodes for the process workflow
G.edge('camera_input', 'feature_extraction', label='Capture Video')
G.edge('feature_extraction', 'nmf_detection', label='Detect NMFs')
G.edge('nmf_detection', 'svm_model', label='NMF to Features')
G.edge('svm_model', 'entropy_calc', label='Classify Gestures')
G.edge('entropy_calc', 'language_processing', label='Text Translation')
G.edge('language_processing', 'text_output', label='Generate Text')
G.edge('svm_model', 'isl_dataset', label='Training Model')
G.edge('text_output', 'text_database', label='Store Translated Text')

# Connect Frontend and Backend
G.edge('web_app', 'camera_input', label='User Input')
G.edge('text_output', 'web_app', label='Display Translated Text')

# Render the graph
G.render('isl_translation_workflow', format='png', view=True)
