# if you dont use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()


import streamlit as st

st.set_page_config(page_title="Agicent Agentic UI", layout="centered")
st.title("Agentic Chatbot Agents")
st.write("Create and Interact with the AI Agents!")
st.markdown(
    """
    <style>
        body {
        }

        .stApp {
        }
        
    </style>
    """,
    unsafe_allow_html=True
)
system_prompt=st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama3-70b-8192", "llama-3.1-8b-instant"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider=st.radio("Select Provider:", ("Groq","OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search=st.checkbox("Allow Web Search")

user_query=st.text_area("Enter your query: ", height=150, placeholder="Ask Anything!")

# API_URL="http://127.0.0.1:9999/chat"
API_URL = "https://python-ai-1-al2j.onrender.com/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        #Step2: Connect with backend via URL
        import requests

        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response=requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")