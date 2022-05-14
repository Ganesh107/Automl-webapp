import streamlit as st
import pandas as pd
import pickle

catboost_model = pickle.load(open('/home/user/Desktop/autoML-webapp/catboost_model/catboost.sav','rb'))
def app():
    st.subheader("DIABETES PREDICTOR")
    pregnancies = st.text_input("Number of Pregnancies")
    glucose = st.text_input("Enter glucose level")
    bp = st.text_input("Enter Blood Pressure level")
    skinthickness = st.text_input("Enter SkinThickness")
    ins = st.text_input("Enter insulin level")
    bmi = st.text_input("Enter Body Mass Index")
    dpf = st.text_input("Enter Diabtes Pedigree Function value")
    age = st.text_input("Enter Age")
    if st.button("Check Result"):
        st.success(diabetes_checker(pregnancies,glucose,bp,skinthickness,ins,bmi,dpf,age))

def diabetes_checker(preg,glu,bp,sT,ins,bmi,dp,age):
    input = [preg,glu,bp,sT,ins,bmi,dp,age]
    prediction = catboost_model.predict(input)
    if prediction == 0:
        return "Not Diabetic"
    else:
        return "Diabetic"