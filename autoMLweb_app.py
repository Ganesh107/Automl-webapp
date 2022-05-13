import streamlit as st
from multiplepages import Multipage
from pages import data_upload,data_preprocess,data_visualize,machine_learning,diabetes_prediction

app = Multipage()

st.title('AUTOML-WEB APPLICATION')

app.add_page('Dataset Details', data_upload.app)
app.add_page('Data Pre-processing', data_preprocess.app)
app.add_page('Data Visualization', data_visualize.app)
app.add_page('Machine Learning', machine_learning.app)
app.add_page('Diabetes Prediction',diabetes_prediction.app)
app.run()   