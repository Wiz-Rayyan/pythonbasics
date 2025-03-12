from diagrams import Diagram, Cluster
from diagrams.custom import Custom

# Create a flowchart diagram
with Diagram("Benefits of ISL Translator", show=True):

    main_benefit = Custom("Benefits of ISL Translator", "./icons/benefit.png")

    with Cluster("Benefits"):
        access = Custom("Increased Accessibility\n- Bridges communication gaps\n- Improves access to information", "./icons/access.png")
        education = Custom("Educational Advancements\n- Supports deaf education\n- Provides learning tools", "./icons/education.png")
        employment = Custom("Employment Opportunities\n- Enhances employability\n- Makes workplaces accessible", "./icons/job.png")
        multilingual = Custom("Multilingual Support\n- Captions in English and Hindi\n- Broadens user base", "./icons/multilang.png")
        empowerment = Custom("Community Empowerment\n- Empowers deaf individuals\n- Enhances societal participation", "./icons/community.png")

    # Define relationships
    main_benefit >> access
    main_benefit >> education
    main_benefit >> employment
    main_benefit >> multilingual
    main_benefit >> empowerment
