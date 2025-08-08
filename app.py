import streamlit as st

# Import your other pages here
from conversation_analysis import conversation_analysis_page
from image_analysis import image_analysis_page

# Configure page layout and title
st.set_page_config(page_title="Multi-Modal AI Playground", layout="wide")
st.title("Multi-Modal AI Playground")

# Sidebar skill selector
skill = st.sidebar.selectbox(
    "Choose AI Skill",
    ["Conversation Analysis", "Image Analysis", "Summarization"]
)

# Render the page based on the selected skill
if skill == "Conversation Analysis":
    conversation_analysis_page()
elif skill == "Image Analysis":
    image_analysis_page()       # you need to implement similarly for images
elif skill == "Summarization":
    summarization_page()        # implement similarly

