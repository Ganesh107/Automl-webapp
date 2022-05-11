import streamlit as st
import pandas as pd

def app():
    st.subheader("UPLOAD DATASET")
    uploaded_file = st.file_uploader("Upload a CSV file ")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.info(format(uploaded_file))
        
        #dataset shape
        if st.button("Dataset shape"):
            st.write(data.shape)
            st.write('Number of rows = ',data.shape[0])
            st.write('Number of columns = ',data.shape[1])

        #view dataset
        if st.checkbox("View dataset"):
            num = st.number_input('Select number of rows',value=5)
            st.write(data.head(num))

        #display columns 
        if st.button("Display columns"):   
            st.write(data.columns)

        #display summary
        if st.button("Summary"):
            st.write(data.describe().T)

        #Value counts
        if st.checkbox("Column Value counts"):
            target = st.text_input("Enter column name (Blank space is not allowed)")
            if(target in data.columns):
                st.write(data[target].value_counts())
            else:
                st.warning("Invalid input")
                st.error("Please enter the correct column name")