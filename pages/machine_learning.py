import numpy
import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title("Build Machine Learning Models")
    st.subheader("UPLOAD DATASET")
    uploaded_file = st.file_uploader("Upload a CSV file ")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
    
        #Model selection
        model_name = st.sidebar.selectbox("Select Classifier",("KNN","SVM","Random Forest"))
        target = st.text_input("Enter target class")
        if target not in data.columns:
            st.warning("Enter Correct Column name")
            st.error("Invalid Column name")
        else:
            x = data.drop(columns=target,axis=1)
            y = data[target]
            st.write("Number of classes = ",len(np.unique(y)))