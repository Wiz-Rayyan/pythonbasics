from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

# Create a horizontal flowchart diagram
with Diagram("Benefits of ISL Translator", show=True):

    main_benefit = Custom("Benefits of ISL Translator", "./icons/benefit.png")

    with Cluster("Benefits"):
        with Cluster("1. Accessibility"):
            access = Custom("Increased Accessibility", "./icons/access.png")
            access_details = Custom("- Bridges communication gaps\n- Improves access to information", "./icons/access.png")

        with Cluster("2. Education"):
            education = Custom("Educational Advancements", "./icons/education.png")
            education_details = Custom("- Supports deaf education\n- Provides learning tools", "./icons/education.png")

        with Cluster("3. Employment"):
            employment = Custom("Employment Opportunities", "./icons/job.png")
            employment_details = Custom("- Enhances employability\n- Makes workplaces accessible", "./icons/job.png")

        with Cluster("4. Multilingual"):
            multilingual = Custom("Multilingual Support", "./icons/multilang.png")
            multilingual_details = Custom("- Captions in English and Hindi\n- Broadens user base", "./icons/multilang.png")

        with Cluster("5. Empowerment"):
            empowerment = Custom("Community Empowerment", "./icons/community.png")
            empowerment_details = Custom("- Empowers deaf individuals\n- Enhances societal participation", "./icons/community.png")

    # Define relationships horizontally
    main_benefit >> Edge() >> access
    main_benefit >> Edge() >> education
    main_benefit >> Edge() >> employment
    main_benefit >> Edge() >> multilingual
    main_benefit >> Edge() >> empowerment
