from graphviz import Digraph

# Create a new directed graph
G = Digraph('G')

# Subgraph for Services (UI/UX Layer) - Top Cluster
with G.subgraph(name='cluster_UI') as c:
    c.attr(label='User Interface / User Experience')
    c.node('homepage', shape='Mrecord', label='{Homepage|Welcome Screen, Language Selection}')
    c.node('isl_camera_input', shape='Mrecord', label='{Live Camera|Capture ISL Gestures}')
    c.node('translated_text_output', shape='Mrecord', label='{Translated Text|Display in English/Hindi}')
    c.node('history_page', shape='Mrecord', label='{Translation History|View Previous Translations}')
    c.node('settings_page', shape='Mrecord', label='{Settings|User Preferences, Languages, Feedback}')

# Subgraph for App Flow (Backend Layer) - Bottom Cluster
with G.subgraph(name='cluster_AppFlow') as c:
    c.attr(label='App Flow (Backend Logic)')
    c.node('auth_service', shape='Mrecord', label='{Authentication|Login, User Data Management}')
    c.node('data_capture', shape='Mrecord', label='{Data Capture|Receive ISL Gestures}')
    c.node('translation_service', shape='Mrecord', label='{Translation Engine|Process ISL to Text}')
    c.node('database', shape='Mrecord', label='{Database|Store User Data, Translations}')
    c.node('history_management', shape='Mrecord', label='{History Service|Fetch Saved Translations}')
    c.node('settings_handler', shape='Mrecord', label='{Settings Handler|Manage Preferences and Settings}')

# Define edges to show user flow (UI/UX Layer)
G.edge('homepage', 'isl_camera_input', label='Go to Camera')
G.edge('isl_camera_input', 'translated_text_output', label='Show Translation')
G.edge('translated_text_output', 'history_page', label='View History')
G.edge('homepage', 'settings_page', label='Settings')

# Connections for App Flow (Backend Layer)
G.edge('auth_service', 'data_capture', label='Capture Gesture')
G.edge('data_capture', 'translation_service', label='Translate to Text')
G.edge('translation_service', 'database', label='Store Translation')
G.edge('database', 'history_management', label='Retrieve History')
G.edge('settings_handler', 'auth_service', label='Update User Preferences')

# Connect the two clusters together to form a continuous flow
G.edge('history_page', 'history_management', label='Fetch from Backend')
G.edge('settings_page', 'settings_handler', label='Save Settings')

# Render the graph
G.render('isl_ui_ux_app_flow', format='png', view=True)
