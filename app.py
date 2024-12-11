import streamlit as st
from utils.kam_behaviour_analysis import kam_behaviour_analysis

# Streamlit app title
st.title("KAM Behaviour Analysis")

# File uploader for the transcript file
uploaded_file = st.file_uploader("Upload a transcript file", type="txt")

if uploaded_file is not None:
    # Read the content of the uploaded file
    prompt = uploaded_file.name

    # Perform behavior analysis
    feedback, cost = kam_behaviour_analysis(prompt)

    # Display the feedback and cost
    st.subheader("Feedback")
    st.write(feedback)

    st.subheader("Cost")
    st.write(cost)