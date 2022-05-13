import streamlit as st
import pandas as pd

def app():
    st.subheader("DIABETES PREDICTOR")
    st.write("UPLOAD DATASET")    
    uploaded_file = st.file_uploader("Upload a CSV file ")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        