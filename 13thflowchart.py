from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.aws.database import RDS

with Diagram("ISL Live Translation Technology Stack", show=False):
    with Cluster("Frontend"):
        html5 = Custom("HTML5", "./path/to/html5_logo.png")
        css = Custom("CSS/Tailwind CSS", "./path/to/css_logo.png")
        js_react = Custom("JavaScript/React", "./path/to/react_logo.png")

    with Cluster("Backend"):
        django = Custom("Django", "./path/to/django_logo.png")
        django_rest = Custom("Django REST Framework", "./path/to/django_rest_logo.png")
        db = RDS("SQLite/PostgreSQL")

    with Cluster("Processing/Computation"):
        python = Custom("Python", "./path/to/python_logo.png")
        opencv = Custom("OpenCV", "./path/to/opencv_logo.png")
        mediapipe = Custom("Mediapipe/Dlib", "./path/to/mediapipe_logo.png")
        numpy = Custom("NumPy", "./path/to/numpy_logo.png")
        sklearn = Custom("Scikit-learn (SVM)", "./path/to/sklearn_logo.png")
        tensorflow = Custom("TensorFlow/PyTorch", "./path/to/tensorflow_logo.png")

    # Workflow Connections
    html5 >> Edge(label="captures") >> js_react
    js_react >> Edge(label="sends video") >> django
    django >> Edge(label="processes data") >> opencv
    opencv >> Edge(label="extracts frames") >> python
    opencv >> Edge(label="background subtraction") >> tensorflow
    mediapipe >> Edge(label="detects features") >> python
    sklearn >> Edge(label="classifies gestures") >> django
    django >> Edge(label="sends output") >> js_react
