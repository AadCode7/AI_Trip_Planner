import streamlit as st
import datetime
import requests
import sys

BASE_URL = "http://localhost:8000"

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌴",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("Travel Smart with AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.header("Tell me where you wanna go and I'll sort everything out!")

with st.form(key="query_form", clear_on_submit=True):
    user_input = st.text_input("~ Search ~", placeholder = "eg. Plan a 5 day trip to Goa")
    submit_button = st.form_submit_button(label="Submit")

if submit_button and user_input.strip():
    try:
        with st.spinner("Calling my contact travel guides in the areas..."):
            payload = {"question": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload)

        if response.status_code == 200:
            answer = response.json().get("answer", "No answer returned")
            markdown_content = f"""AI Travel Plan
    
            # **Generated:** {datetime.datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}
            # **Created By:** AI Travel Planner
            ---
            {answer}    
            """
            st.markdown(markdown_content, unsafe_allow_html=True)

        else:
            st.error(f"Status code not 200: {response.status_code} - {response.text}")

    except Exception as e:
        raise f"Response failed due to: {e}"

#1:18:56