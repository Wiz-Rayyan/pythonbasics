from graphviz import Digraph

dot = Digraph()

# Main application block
dot.node('A', 'AI-Driven Digital Forensics Application', shape='rectangle')

# User Interface
dot.node('B', 'User Interface (UI)', shape='rectangle')
dot.edge('A', 'B')

# File Upload
dot.node('C', 'File Upload', shape='rectangle')
dot.edge('B', 'C')

# File Validation
dot.node('D', 'File Validation', shape='rectangle')
dot.edge('C', 'D')

# Metadata Extraction
dot.node('E', 'Metadata Extraction', shape='rectangle')
dot.edge('D', 'E')

# Content Segmentation
dot.node('F', 'Content Segmentation', shape='rectangle')
dot.edge('E', 'F')

# Data Preprocessing
dot.node('G', 'Data Preprocessing', shape='rectangle')
dot.edge('F', 'G')

# Feature Extraction
dot.node('H', 'Feature Extraction', shape='rectangle')
dot.edge('G', 'H')

# AI Algorithms
dot.node('I', 'AI Algorithms', shape='ellipse')
dot.edge('H', 'I')

# Image Analysis
dot.node('J', 'Image Analysis (CNN)', shape='rectangle')
dot.edge('I', 'J')

# Video Analysis
dot.node('K', 'Video Analysis (RNN/LSTM)', shape='rectangle')
dot.edge('I', 'K')

# Text Analysis
dot.node('L', 'Text Analysis (Transformers)', shape='rectangle')
dot.edge('I', 'L')

# Audio Analysis
dot.node('M', 'Audio Analysis (MFCCs)', shape='rectangle')
dot.edge('I', 'M')

# Ensemble Learning
dot.node('N', 'Ensemble Learning', shape='rectangle')
dot.edge('I', 'N')

# Content Classification
dot.node('O', 'Content Classification', shape='rectangle')
dot.edge('J', 'O')
dot.edge('K', 'O')
dot.edge('L', 'O')
dot.edge('M', 'O')
dot.edge('N', 'O')

# Reporting
dot.node('P', 'Reporting', shape='rectangle')
dot.edge('O', 'P')

# Data Storage
dot.node('Q', 'Data Storage', shape='rectangle')
dot.edge('P', 'Q')

# Real-time Processing
dot.node('R', 'Real-time Processing (Kafka/Flink)', shape='rectangle')
dot.edge('A', 'R')

# Save and render the diagram
dot.render('digital_forensics_diagram', format='png', cleanup=True)
