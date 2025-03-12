from diagrams import Cluster, Diagram
from diagrams.aws.ml import SagemakerModel
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.generic.storage import Storage
from diagrams.aws.analytics import KinesisDataStreams
from diagrams.onprem.monitoring import Prometheus
from diagrams.generic.network import Firewall

with Diagram("ISL Translator Workflow", show=False):
    user = User("ISL User")
    admin = User("Admin")

    with Cluster("Translation System"):
        camera = Server("Video Input")
        firewall = Firewall("Input Filter")
        model = SagemakerModel("Sign Recognition Model")
        database = PostgreSQL("NMFs Database")
        redis_cache = Redis("Cache")
        error_handler = Server("Error Detection")
        text_output = Server("Text Output")
        feedback_system = KinesisDataStreams("Feedback for Training")

    with Cluster("Monitoring & Logging"):
        monitoring = Prometheus("Performance Monitoring")
        logs = Storage("System Logs")

    storage = Storage("Captioned Output")
    
    user >> camera >> firewall >> model
    model >> redis_cache
    redis_cache >> database
    model >> text_output
    text_output >> storage

    model >> error_handler >> feedback_system
    feedback_system >> admin

    model >> monitoring
    monitoring >> logs
    error_handler >> logs
