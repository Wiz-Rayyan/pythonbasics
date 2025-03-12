from diagrams import Cluster, Diagram
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.aws.ml import SagemakerModel
from diagrams.onprem.analytics import Spark
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.network import Nginx
from diagrams.onprem.inmemory import Redis
from diagrams.aws.storage import S3

with Diagram("ISL Live Translation Workflow", show=False):
    # User Interface: Start ISL Video / Live Feed
    user = User("User Interface")
    live_feed = Server("Start ISL Video / Live Feed")

    with Cluster("Backend Processing"):
        frame_capture = Server("Frame Capture")
        preprocessing = Server("Preprocessing")
        nmf_detection = SagemakerModel("NMF Detection (OpenCV, Dlib, MediaPipe)")
        feature_extraction = Server("Feature Extraction")
        translation = Spark("Contextual Translation")
        text_generation = Server("Text Generation (English/Hindi)")

    # Output: Display Translated Text
    output = Server("Display Translated Text")

    # Flow connections
    user >> live_feed >> frame_capture >> preprocessing >> nmf_detection >> feature_extraction >> translation >> text_generation >> output
