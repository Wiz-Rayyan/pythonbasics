from diagrams import Cluster, Diagram, Edge
from diagrams.aws.ml import Rekognition  # Using these for example, replace with general blocks as needed
from diagrams.generic.blank import Blank

with Diagram("ISL Live Translation Workflow", show=False):
    
    # User Interface Section
    user_input = Blank("Start ISL Video / Live Feed")
    
    # Backend Processing Section
    with Cluster("Backend Processing"):
        # Step 1: Frame Capture
        frame_capture = Blank("Frame Capture")

        # Step 2: Preprocessing
        preprocessing = Blank("Preprocessing (Resizing, Noise Reduction, Color Correction)")
        
        # Step 3: NMF Detection
        nmf_detection = Blank("NMF Detection (Facial Expressions, Head Movements, Body Gestures)")
        
        # Step 4: Feature Extraction
        feature_extraction = Blank("Feature Extraction (Hand Gestures, NMFs)")
        
        # Step 5: Contextual Translation
        contextual_translation = Blank("Contextual Translation (Meaning based on Gestures and Expressions)")
        
        # Step 6: Text Generation
        text_generation = Blank("Text Generation (English/Hindi)")
        
    # Output Section
    display_output = Blank("Display Translated Text (Real-Time Captions/Subtitles)")
    
    # Flow Connections
    user_input >> frame_capture >> preprocessing >> nmf_detection >> feature_extraction >> contextual_translation >> text_generation >> display_output
