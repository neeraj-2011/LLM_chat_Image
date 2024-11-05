# Importing necessary libraries
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Get the API key from the environment variable injected by GitHub Codespaces
GOOGLE_API_KEY = os.getenv("GOOGLE_KEY")

# Check if API key is available
if GOOGLE_API_KEY is None:
    st.error("API Key not found. Please set the GOOGLE_KEY environment variable.")
else:
    # Configure the Google Gemini API with the key
    genai.configure(api_key=GOOGLE_API_KEY)

    # Function to get Gemini API response based on user input and uploaded image
    def get_gemini_response(input, image):
        model = genai.GenerativeModel('gemini-1.5-flash')
        if input != "":
            response = model.generate_content([input, image])
        else:
            response = model.generate_content(image)
        return response.text

    # Initialize the Streamlit app
    st.set_page_config(page_title="Gemini Image Demo")
    st.header("NeerajAI: Image Insights Application")

    st.header("Gemini Image Demo")

    st.write("""
    Welcome to the Gemini Image Demo!

    This is a simple app where you can upload an image, and the AI will describe it for you. Just choose an image, and the app will generate a detailed description based on what it sees.

    Try it out and see how AI can interpret and describe your images!
    """)


    # User input prompt and image upload
    input = st.text_input("Input Prompt: ", key="input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Initialize image variable
    image = ""   
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    # Submit button for processing
    submit = st.button("Tell me about the image")

    # If submit button is clicked
    if submit:
        if uploaded_file is not None:
            response = get_gemini_response(input, image)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Please upload an image to proceed.")

