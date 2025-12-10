# QA_conditional_input.py
from dotenv import load_dotenv
load_dotenv()

import os
from PIL import Image
import streamlit as st
import google.generativeai as genai
import io

# Configure API key
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    st.error("No GOOGLE_API_KEY found in environment. Put it in your .env file.")
    st.stop()

genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Gemini Vision — Conditional Q Input", layout="centered")
st.title("Gemini Vision — Upload image and ask Question")

# Sidebar (optional)
selected_model = st.sidebar.text_input("Model name (exact):", value="models/gemini-2.5-flash")

# 1) Image upload
uploaded_file = st.file_uploader("Upload an image (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

pil_img = None
if uploaded_file is not None:
    try:
        pil_img = Image.open(uploaded_file).convert("RGB")
        st.image(pil_img, caption="Uploaded image", use_column_width=True)
    except Exception as e:
        st.error(f"Failed to open image: {e}")
        pil_img = None

# 2) Show text input ONLY after image has been uploaded successfully
user_input = ""
if pil_img is not None:
    user_input = st.text_input("Enter your question :", value="", key="question_input")

# Helper: prepare image for the model (pass PIL directly)
def get_image_for_model(pil_image):
    return pil_image  # most genai SDKs accept PIL.Image.Image

# 3) Generate button (only enabled when image exists)
if st.button("Generate Response"):
    if pil_img is None:
        st.error("Please upload an image first.")
    else:
        try:
            gen_model = genai.GenerativeModel(selected_model)
        except Exception as e:
            st.error(f"Failed to create model object for '{selected_model}': {e}")
            st.stop()

        try:
            image_part = get_image_for_model(pil_img)
            if user_input.strip() != "":
                response = gen_model.generate_content([user_input, image_part])
            else:
                response = gen_model.generate_content(image_part)

            # extract text safely
            try:
                text = response.text
            except Exception:
                # fallback extraction for other response shapes
                text = None
                try:
                    result = getattr(response, "result", None)
                    if result and getattr(result, "candidates", None):
                        text = result.candidates[0].content.parts[0].text
                except Exception:
                    text = None

            if text:
                st.subheader("Answer")
                st.write(text)
            else:
                st.error("Couldn't extract text from the model response. Enable debugging in a different version if needed.")

        except Exception as e:
            st.error(f"Error calling generate_content: {e}")
