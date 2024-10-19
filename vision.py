import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(girdi,image):
    if girdi != "":
        response = model.generate_content([girdi,image])
    else:
        response = model.generate_content(image)

    return response.text

st.set_page_config(page_title="Gemini image demo")
st.header("Gemini application")
input_text = st.text_input("input prompt : ",key = "input_text")


uploaded_file = st.file_uploader("choose an image...",type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="uploaded image.",use_column_width=True)


submit_button = st.button("show")

# if submit is clicked
if submit_button:
    response = get_gemini_response(input_text,image)
    st.subheader("the response is")
    st.write(response)



