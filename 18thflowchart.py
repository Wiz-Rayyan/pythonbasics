from diagrams import Diagram, Cluster, Edge, Node

# Start the flowchart
with Diagram("ISL Live Translation Technology Stack", show=True, filename="isl_translation_stack"):
    start = Node("Webcam input")

    with Cluster("Frontend"):
        html5 = Node("HTML5\n(Handling Video Input)")
        css = Node("CSS/Tailwind CSS\n(Styling Interface)")
        js_react = Node("React\n(Dynamic UI)")

    with Cluster("Backend"):
        django = Node("Django\n(Server-side Logic)")
        django_rest = Node("Django REST Framework\n(API Endpoints)")

    with Cluster("Processing & Computation"):
        python = Node("Python\n(Video Processing)")
        opencv = Node("OpenCV\n(Frame Capture)")
        mediapipe = Node("Mediapipe/Dlib\n(Feature Detection)")
        numpy = Node("NumPy\n(Matrix Operations)")
        sklearn = Node("Scikit-learn (SVM)\n(Gesture Classification)")
        tensorflow = Node("TensorFlow & PyTorch\n(Advanced Features)")

    with Cluster("Database"):
        db = Node("SQLite/PostgreSQL\n(Data Storage)")

    with Cluster("Output"):
        react_output = Node("Django Templates/React\n(Rendering Output)")
        html_css = Node("HTML/CSS\n(Display of styled Translated Text)")

    # Workflow Connections
    start >> Edge(label="Initializes") >> html5
    html5 >> Edge(label="captures video") >> js_react
    js_react >> Edge(label="sends data") >> django
    django >> Edge(label="processes") >> opencv
    opencv >> Edge(label="captures frames") >> python
    opencv >> Edge(label="background subtraction") >> tensorflow
    mediapipe >> Edge(label="detects features") >> python
    python >> Edge(label="processes data") >> sklearn
    django >> Edge(label="stores data") >> db
    django >> Edge(label="sends output") >> react_output
    react_output >> Edge(label="displays") >> html_css

# Optionally, to enhance clarity, you might consider using a larger font size in your system settings or the diagram's environment.
