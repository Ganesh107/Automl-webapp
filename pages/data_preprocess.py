import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def app():
    st.title("Pre-processing")
    st.subheader("UPLOAD DATASET")
    uploaded_file = st.file_uploader("Upload a CSV file ")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        #display data
        if st.checkbox("View dataset"):
            num = st.number_input('Select number of rows',value=5)
            st.write(data.head(num))

        #count null values
        if st.button("Missing Values"):
            st.write(data.isnull().sum())
        
        #fill missing values
        if st.button("Fill Missing values"):
            if(data.isnull().sum() is True):
                data.fillna(data.mean(),inplace=True)
                st.write(data.isnull().sum())
            else:
                st.warning("Dataset does not contain null values")

        #standardization
        st.subheader("Standardize data")
        if st.checkbox("Use Standard scaler"):
            target = st.text_input("Enter Target class")
            if(target in data.columns):
                scaler = StandardScaler()
                cols_to_scale = data.drop([target],axis=1)
                y = data[target]
                std_diabetes_data = scaler.fit_transform(cols_to_scale)
                std_diabetes_data = pd.DataFrame(data=std_diabetes_data,columns=data.columns[:-1])
                std_diabetes_data[target] = data[target]
                st.write(std_diabetes_data.head(5))
                st.write("SUMMARY")
                st.write(std_diabetes_data.describe().T)

                #Cache the conversion to prevent conversion on every rerun
                @st.cache
                def convert_df(df):
                    return df.to_csv()

                csv = convert_df(std_diabetes_data)
                st.download_button(
                label="Download Pre-processed dataset",
                data=csv,
                file_name='pre_processed_dataset.csv',
                mime='text/csv')
            else:
                st.warning("Invalid input")
                st.error("Please enter the correct column name")
