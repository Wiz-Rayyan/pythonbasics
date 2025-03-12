from graphviz import Digraph

# Create a new directed graph
G = Digraph('G')

# Subgraph cluster for Services (Frontend/UI Layer)
with G.subgraph(name='cluster_Services') as c:
    c.attr(label='ISL Translation System (Frontend/UI)')
    c.node('isl_app', shape='Mrecord', label='{ISL App|Capture and Translate ISL}')

# Subgraph cluster for Server1 and Jobs (Processing/AI Layer)
with G.subgraph(name='cluster_Server1') as c:
    c.attr(label='Processing Server (AI/ML)')
    with c.subgraph(name='cluster_Jobs') as jobs:
        jobs.attr(label='AI/ML Processing')
        jobs.node('job_gesture_analysis', shape='Mrecord', label='{Gesture Analysis|Step 1) Run ISL Model}')
        jobs.node('job_translation', shape='Mrecord', label='{Translation Process|Step 2) Generate Text}')

# Subgraph cluster for Server2, Support_Database, Procs, Tables, and Views (Database Layer)
with G.subgraph(name='cluster_Server2') as c:
    c.attr(label='Server2 (Database Layer)')
    with c.subgraph(name='cluster_Support_Database') as support_db:
        support_db.attr(label='User and Translation Data')
        with support_db.subgraph(name='cluster_Procs') as procs:
            procs.attr(label='Stored Procedures')
            procs.node('usp_CaptureGesture')
            procs.node('usp_StoreTranslation')
        with support_db.subgraph(name='cluster_Tables') as tables:
            tables.attr(label='Tables')
            tables.node('GestureTable', label='Captured Gestures')
            tables.node('TranslationTable', label='Stored Translations')
        with support_db.subgraph(name='cluster_Views') as views:
            views.attr(label='Views')
            views.node('vw_UserHistory', label='User Translation History')

# Subgraph cluster for Server3 and AutoAlert_Support (Notification Layer)
with G.subgraph(name='cluster_Server3') as c:
    c.attr(label='Server3 (Notification Layer)')
    with c.subgraph(name='cluster_AutoAlert_Support') as auto_alert:
        auto_alert.attr(label='Notification System')
        with auto_alert.subgraph(name='cluster_Procs') as procs:
            procs.attr(label='Stored Procedures')
            procs.node('usp_SendNotifications')
            procs.node('usp_UserAlerts')

# Subgraph cluster for Reports (Reporting Layer)
with G.subgraph(name='cluster_Reports') as c:
    c.attr(label='Report Server')
    c.node('user_activity_report', shape='Mrecord', label='{User Activity Report|Translation Logs}')
    c.node('system_performance_report', shape='Mrecord', label='{System Performance|Logs}')

# Define edges between nodes
G.edge('isl_app', 'usp_CaptureGesture')
G.edge('usp_CaptureGesture', 'GestureTable')
G.edge('usp_StoreTranslation', 'TranslationTable')
G.edge('job_gesture_analysis', 'job_translation')

G.edge('job_gesture_analysis', 'usp_StoreTranslation')
G.edge('job_translation', 'TranslationTable')

G.edge('usp_SendNotifications', 'vw_UserHistory')
G.edge('usp_UserAlerts', 'vw_UserHistory', style='dashed')

G.edge('user_activity_report', 'usp_StoreTranslation')
G.edge('system_performance_report', 'usp_CaptureGesture')

# Render the graph
G.render('isl_translation_system', format='png', view=True)
