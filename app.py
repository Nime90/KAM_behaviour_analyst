import streamlit as st
from utils.kam_behaviour_analysis import kam_behaviour_analysis
from utils.read_text import read_text_with_gtts
from utils.feedback_summary import feedback_summary

# Streamlit app title
st.title("KAM Behaviour Analysis")

# File uploader for the transcript file
uploaded_file = st.file_uploader("Upload a transcript file", type="txt")

if uploaded_file is not None:
    # Read the content of the uploaded file
    prompt = uploaded_file.read().decode("utf-8")

    # Perform behavior analysis
    feedback, cost = kam_behaviour_analysis(prompt)

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

    
