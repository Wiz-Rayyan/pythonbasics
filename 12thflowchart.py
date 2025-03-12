'''

from diagrams import Cluster, Diagram, Edge
from diagrams.programming.language import Python, JavaScript
from diagrams.onprem.client import User
from diagrams.onprem.database import PostgreSQL

from diagrams.onprem.framework import Django # type: ignore
from diagrams.onprem.ml import Tensorflow # type: ignore

from diagrams.programming.framework import React

with Diagram("Technology Stack for ISL Live Translation", show=False):
    
    # User Interface Section
    user = User("User")
    
    with Cluster("Frontend"):
        frontend_html = JavaScript("HTML5")
        frontend_css = JavaScript("CSS/Tailwind CSS")
        frontend_js = React("React/JavaScript")
    
    with Cluster("Backend"):
        django_backend = Django("Django")
        django_rest = Django("Django REST Framework")
        sqlite_postgres = PostgreSQL("SQLite/PostgreSQL")
        
    with Cluster("Processing/Computation"):
        python_processing = Python("Python")
        opencv = Python("OpenCV")
        mediapipe = Python("Mediapipe/Dlib")
        numpy = Python("NumPy")
        sklearn = Python("Scikit-learn (SVM)")
        tensorflow_pytorch = Tensorflow("TensorFlow/PyTorch")
    
    # Flow Connections for Processing Layers
    user >> Edge(label="Video Feed") >> frontend_html
    frontend_html >> Edge(label="Sends Video") >> django_backend >> opencv
    opencv >> Edge(label="Frame Extraction") >> python_processing
    python_processing >> Edge(label="Background Subtraction") >> tensorflow_pytorch
    tensorflow_pytorch >> Edge(label="Feature Extraction") >> mediapipe
    mediapipe >> Edge(label="Gesture Recognition") >> sklearn
    sklearn >> Edge(label="Text Conversion") >> django_backend
    
    # Connect Database and Output
    sklearn >> Edge(label="Stores Translations") >> sqlite_postgres
    django_backend >> Edge(label="Sends Text") >> frontend_js
    frontend_js >> Edge(label="Renders Translated Text") >> user
'''