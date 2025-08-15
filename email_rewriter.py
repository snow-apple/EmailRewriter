import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai_api_key = os.getenv("openai_api_key")
client = OpenAI(api_key=openai_api_key)


st.markdown("""
    <style>
    /* App background */
    .stApp {
        background-color: #fce6f6;
        font-family: 'Arial', sans-serif;
    }
    /* Header */
    h1 {
        color: #edc4f5;
        text-align: center;
    }
    /* Button style */
    div.stButton > button:first-child {
        background-color: #95e4f0;
        color: white;
        height: 3em;
        width: 100%;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
    }
    /* Text areas */
    textarea {
        background-color: #95e4f0;
        font-size: 14px;
    }
""", unsafe_allow_html=True)


st.markdown("<h1>Smart Email Rewriter</h1>", unsafe_allow_html=True)
st.write("---")

st.subheader("Email Rewriting")
email_text = st.text_area("Paste your email here:")
tone = st.selectbox("Choose tone:", ["Friendly", "Formal", "Concise", "Persuasive", "Playful", "Serious"])

if st.button("Click to Rewrite"):
    prompt = f"Rewrite the following email in a {tone.lower()} tone:\n\n{email_text}"

    with st.spinner("Rewriting your email... ⏳"):
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {"role": "system", "content": "You are an expert email editor."},
                {"role": "user", "content": prompt}
            ]
        )

    rewritten_email = response.choices[0].message.content

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Email")
        st.write(email_text)

    with col2:  
        st.subheader("Rewritten Email")
        st.markdown(
            f"<div style='background-color:#f0f8ff; padding:10px; border-radius:10px'>{rewritten_email}</div>",
            unsafe_allow_html=True
        )
