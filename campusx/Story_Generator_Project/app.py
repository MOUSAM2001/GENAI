import streamlit as st
from PIL import Image
from image_to_story_generator import generate_story_from_images

st.title("Story Generator from Images")
st.markdown("Upload 1 to 10 images,choose an style and let AI write and narrate an story for you.")

with st.sidebar:
    st.header("Controls")

    uploaded_files = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

    style = st.selectbox("Choose Story Style", ["Technology","Mystery", "Murder", "Horror"])

    # generate button

    generate_button = st.button("Generate Story")

if generate_button:
    if not uploaded_files:
        st.warning("Please upload at least one image.")
    elif len(uploaded_files) > 15:
        st.warning("Please upload no more than 15 images.")
    else:
        with st.spinner(f"Generating a {style} story for {len(uploaded_files)} images..."):

            try:
                pillow_images = [Image.open(file) for file in uploaded_files]
                st.subheader("Your Uploaded Images:")
                image_columns = st.columns(len(pillow_images))
                for i,image in enumerate(pillow_images):
                    image_columns[i].image(image, width=300)
            except Exception as e:
                st.error(f"Error loading images: {e}")
                st.stop()
            try:
                story_text = generate_story_from_images(pillow_images,style)
            except Exception as e:
                st.error(f"Error generating story: {e}")
                st.stop()
            st.success(story_text)