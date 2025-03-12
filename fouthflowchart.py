from diagrams import Diagram, Edge
from diagrams.generic.blank import Blank

with Diagram("ISL Live Translation Workflow", show=False):
    # User Interface
    start = Blank("Start ISL Video / Live Feed")
    
    # Backend Processing
    frame_capture = Blank("Frame Capture")
    preprocessing = Blank("Preprocessing")
    nmf_detection = Blank("NMF Detection")
    feature_extraction = Blank("Feature Extraction")
    contextual_translation = Blank("Contextual Translation")
    text_generation = Blank("Text Generation")

    # Output
    display_output = Blank("Display Translated Text")

    # Flow connections
    start >> frame_capture >> preprocessing >> nmf_detection >> feature_extraction >> contextual_translation >> text_generation >> display_output
