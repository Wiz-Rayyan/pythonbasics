from graphviz import Digraph

# Create a new directed graph
G = Digraph('G')

# Subgraph cluster for Services
with G.subgraph(name='cluster_Services') as c:
    c.attr(label='Services')
    c.node('app_foobar', shape='Mrecord', label='{Foobar Repo|.Net App}')

# Subgraph cluster for Server1 and Jobs
with G.subgraph(name='cluster_Server1') as c:
    c.attr(label='Server1')
    with c.subgraph(name='cluster_Jobs') as jobs:
        jobs.attr(label='Jobs')
        jobs.node('job_daily', shape='Mrecord', label='{Job) Daily Job|Step 2) Run stored proc}')

# Subgraph cluster for Server2, Support_Database, Procs, Tables, and Views
with G.subgraph(name='cluster_Server2') as c:
    c.attr(label='Server2')
    with c.subgraph(name='cluster_Support_Database') as support_db:
        support_db.attr(label='Support_Database')
        with support_db.subgraph(name='cluster_Procs') as procs:
            procs.attr(label='Procs')
            procs.node('usp_StoredProcedure1')
            procs.node('usp_StoredProcedure2')
        with support_db.subgraph(name='cluster_Tables') as tables:
            tables.attr(label='Tables')
            tables.node('Table1')
            tables.node('Table2')
            tables.node('Table3')
            tables.node('Table4')
        with support_db.subgraph(name='cluster_Views') as views:
            views.attr(label='Views')
            views.node('vw_View1')

# Subgraph cluster for Server3 and AutoAlert_Support
with G.subgraph(name='cluster_Server3') as c:
    c.attr(label='Server3')
    with c.subgraph(name='cluster_AutoAlert_Support') as auto_alert:
        auto_alert.attr(label='Other_Database')
        with auto_alert.subgraph(name='cluster_Procs') as procs:
            procs.attr(label='Procs')
            procs.node('usp_StoredProcedure3')
            procs.node('usp_StoredProcedure4')

# Subgraph cluster for Reports
with G.subgraph(name='cluster_Reports') as c:
    c.attr(label='Report Server')
    c.node('ssrs_report_1', shape='Mrecord', label='{SSRS Report 1|ReportFile1.rdl}')
    c.node('ssrs_report_2', shape='Mrecord', label='{SSRS Report 2|ReportFile2.rdl}')

# Define edges between nodes
G.edge('app_foobar', 'usp_StoredProcedure1')
G.edge('usp_StoredProcedure1', 'Table1')
G.edge('usp_StoredProcedure1', 'Table2')
G.edge('usp_StoredProcedure1', 'Table3')

G.edge('usp_StoredProcedure2', 'Table4')
G.edge('usp_StoredProcedure2', 'Table3', color='red')

G.edge('job_daily', 'usp_StoredProcedure2')

G.edge('ssrs_report_1', 'usp_StoredProcedure3')
G.edge('ssrs_report_2', 'usp_StoredProcedure4')

G.edge('usp_StoredProcedure3', 'vw_View1', style='dashed')
G.edge('usp_StoredProcedure4', 'vw_View1', style='dashed')

G.edge('vw_View1', 'Table1', style='dashed')
G.edge('vw_View1', 'Table2', style='dashed')
G.edge('vw_View1', 'Table3', style='dashed')

# Render the graph
G.render('11th', format='png', view=True)
