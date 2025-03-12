from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

# Create a flowchart diagram
with Diagram("Benefits of ISL Translator", show=True):

    # Main Benefit
    main_benefit = Custom("Benefits of ISL Translator", "./icons/benefit.png")

    with Cluster("Increased Accessibility"):
        access_1 = Custom("Bridges communication gaps", "./icons/access.png")
        access_2 = Custom("Improves access to information", "./icons/access.png")

    with Cluster("Educational Advancements"):
        education_1 = Custom("Supports deaf education", "./icons/education.png")
        education_2 = Custom("Provides tools for better learning", "./icons/education.png")

    with Cluster("Employment Opportunities"):
        job_1 = Custom("Enhances employability", "./icons/job.png")
        job_2 = Custom("Makes workplaces more accessible", "./icons/job.png")

    with Cluster("Multilingual Support"):
        multi_1 = Custom("Captions in English and Hindi", "./icons/multilang.png")
        multi_2 = Custom("Broadens user base", "./icons/multilang.png")

    with Cluster("Community Empowerment"):
        empower_1 = Custom("Empowers deaf individuals", "./icons/community.png")
        empower_2 = Custom("Enhances participation in society", "./icons/community.png")

    # Define relationships
    main_benefit >> Edge() >> access_1
    main_benefit >> Edge() >> access_2
    main_benefit >> Edge() >> education_1
    main_benefit >> Edge() >> education_2
    main_benefit >> Edge() >> job_1
    main_benefit >> Edge() >> job_2
    main_benefit >> Edge() >> multi_1
    main_benefit >> Edge() >> multi_2
    main_benefit >> Edge() >> empower_1
    main_benefit >> Edge() >> empower_2
