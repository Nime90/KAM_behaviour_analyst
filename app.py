import streamlit as st
from utils.kam_behaviour_analysis import kam_behaviour_analysis
from utils.read_text import read_text_with_gtts
from utils.feedback_summary import feedback_summary
import requests
from PIL import Image
from io import BytesIO

# Streamlit app title
st.title("FeedBecca")
response = requests.get("https://drive.usercontent.google.com/download?id=11K9B3lCLc-1yoLUbKTSZgZYCrJS92dCQ&authuser=0")
response.raise_for_status()
image = Image.open(BytesIO(response.content))
st.image(image, caption="Feedbacca", use_column_width=False)
st.write("Hi, I am FeedBecca!:wave: ")
st.write("A friendly assistant that helps you evaluating your conversation with the coach!")

# File uploader for the transcript file
uploaded_file = st.file_uploader("Please upload the transcript of the conversation with your coach here!", type="txt")

if uploaded_file is not None:
    # Read the content of the uploaded file
    prompt = uploaded_file.read().decode("utf-8")

    # Perform behavior analysis
    feedback, cost = kam_behaviour_analysis(prompt,best_practices_core_competences, best_practices_content_Monthly, Behavioural_Expectations)

    # Display the feedback and cost
    st.subheader("Feedback")
    st.write(feedback)

    st.subheader("Cost")
    st.write(cost)
    if feedback:
        feedback_summarized, cost  = feedback_summary(feedback, model="gpt-4o")
        summary = str(feedback_summarized)
        
        # Display the feedback and cost
        st.subheader("summary")
        st.write(summary)
        st.write(cost)

        read_text_with_gtts(summary)
    

    
