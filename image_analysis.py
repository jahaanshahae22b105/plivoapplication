import streamlit as st
from utils.image_caption import describe_image

def image_analysis_page():
    st.header("Image Analysis")
    
    # Image upload option
    image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png", "bmp"])
    
    if image_file:
        # Display the uploaded image
        st.image(image_file, caption="Uploaded Image", use_column_width=True)
        
        # Generate and display image description
        with st.spinner("Generating image description..."):
            description = describe_image(image_file)
        st.subheader("Image Description")
        st.write(description)

# Optional: run the page directly for testing
if __name__ == "__main__":
    image_analysis_page()
