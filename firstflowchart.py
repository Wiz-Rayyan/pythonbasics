from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS

with Diagram("Grouped Web Service", show=False):
    with Cluster("Web Cluster"):
        web_servers = [EC2("Web Server 1"), EC2("Web Server 2")]

    lb = ELB("Load Balancer")
    db = RDS("Database")

    lb >> web_servers >> db
