from diagrams import Diagram, Cluster, Edge, Node
from diagrams.custom import Custom 
image_path = r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 142151.png"
htmlimage = r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 160627.png"
tailwindimage = r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 160944.png"

# Start the flowchart
with Diagram("ISL Live Translation Technology Stack", show=True, direction="LR"):
    start2 = Node("UI", fontsize="80", width="2.5", height="1.5")
    start = Custom("Webcam input", r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 165233.png")
    s3 = Custom("text input", r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 170157.png")
    s4 = Custom("For Reverse Translation", r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 171400.png")
   

    with Cluster("Frontend"):
        html5 = Custom("HTML5\n(Handling Video Input)",htmlimage )
        css = Custom("CSS/Tailwind CSS\n(Styling Interface)", tailwindimage)
        js_react = Custom("React\n(Dynamic UI)", r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 162730.png")

    with Cluster("Backend"):
        django = Custom("Django\n(Server-side Logic)", r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 162849.png")
        django_rest = Custom("Django REST Framework\n(API Endpoints)", r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 165127.png")

    with Cluster("Processing & Computation"):
        python = Custom("Python\n(Video Processing)", image_path)
        opencv = Custom("OpenCV\n(Frame Capture)", r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 162955.png")
        mediapipe = Custom("Mediapipe/Dlib\n(Feature Detection)", r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 164332.png")
        numpy = Custom("NumPy\n(Matrix Operations)", r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 164500.png")
        sklearn = Custom("Scikit-learn (SVM)\n(Gesture Classification)", r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 164558.png")
        tensorflow = Custom("TensorFlow & PyTorch\n(Advanced Features)", r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 164718.png")

    with Cluster("Database"):
        db = Custom("SQLite/PostgreSQL\n(Data Storage)", r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 164816.png")

    with Cluster("Output"):
        react_output = Custom("Django Templates/React\n(Rendering Output)", r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 162849.png")
        html_css = Custom("HTML/CSS\n(Display of styled Translated Text)", r"C:\Users\Rayyan\Pictures\Screenshots\Screenshot 2024-09-29 164953.png")

    # Workflow Connections
    start2 >> Edge(label="feature1") >> start
    start2 >> Edge(label="feature2") >> s3
    s3 >> Edge(label="Avatar feature") >> s4
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
