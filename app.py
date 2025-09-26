import streamlit as st
from File_uploader import upload_image
from LLM import analyze_image

st.set_page_config(page_title="Image Analysis App", layout="centered")

st.title("Image Upload & Analysis App")
st.write("Upload an image, and the AI will analyze it for you!")

# File uploader
uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg", "gif"])

if uploaded_file is not None:
    # Show preview
    st.image(uploaded_file, caption="Uploaded Image")

    # Button to upload to Cloudinary
    if st.button("Solve"):
        with st.spinner("Uploading image to Cloudinary..."):
            try:
                # Upload image to Cloudinary
                image_url = upload_image(uploaded_file)
                st.success("Image uploaded to Cloudinary ✅")
                st.write("Image URL:", image_url)
            except Exception as e:
                st.error(f"Cloudinary upload failed: {e}")
                st.stop()

        with st.spinner("Solving Problem ... "):
            try:
                response = analyze_image(image_url)
                st.subheader("API Response")
                st.write(response)
            except Exception as e:
                st.error(f"API request failed: {e}")

