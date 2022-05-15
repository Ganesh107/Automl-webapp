import streamlit as st
import pandas as pd
import numpy as np
import random
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
    if st.checkbox("Check Result"):
        rslt = diabetes_checker(pregnancies,glucose,bp,skinthickness,ins,bmi,dpf,age)
        st.success(rslt)

        if rslt == "Diabetic":
            st.subheader("Check Diet Plan")
            #Calculating BMR
            weight = st.number_input("Enter weight(in kg)")
            height = st.number_input("Enter height(in cm)")
            age = st.number_input("Enter age")
            bmr = (10*weight)+(6.25*height)-(5*age)-161

            if st.checkbox("Check BMR and Required calories"):
                st.write("BMR = ",bmr)    
                #Calculating required calories
                exercise_rate = st.selectbox("Enter exercise rate",['no','light','moderate','hard'])
                if exercise_rate == "no":
                    req_calories = bmr*1.2
                elif exercise_rate == "light":
                    req_calories = bmr*1.375
                elif exercise_rate == "moderate":
                    req_calories = bmr*1.725
                elif exercise_rate == "hard":
                    req_calories = bmr*1.9
                st.write('Required Calories = ',req_calories)

                if(st.checkbox("Check Diet")):
                    data = pd.read_csv('/home/user/Desktop/autoML-webapp/data/input.csv')
                    Breakfastdata=data['Breakfast'] 
                    BreakfastdataNumpy=Breakfastdata.to_numpy()
                            
                    Lunchdata=data['Lunch']
                    LunchdataNumpy=Lunchdata.to_numpy()
                            
                    Dinnerdata=data['Dinner']
                    DinnerdataNumpy=Dinnerdata.to_numpy()
                            
                    Food_itemsdata=data['Food_items'] #food item names
                    breakfastfoodseparated=[]
                    Lunchfoodseparated=[]
                    Dinnerfoodseparated=[]
                            
                    #seperating different foods 
                    for i in range(len(Breakfastdata)):
                        if BreakfastdataNumpy[i]==1:
                            breakfastfoodseparated.append(Food_itemsdata[i])
                        if LunchdataNumpy[i]==1:
                            Lunchfoodseparated.append(Food_itemsdata[i])
                        if DinnerdataNumpy[i]==1:
                            Dinnerfoodseparated.append(Food_itemsdata[i])


                    #creating food_dataframes along with calories
                    bfast = pd.DataFrame(breakfastfoodseparated)
                    bfast['Calories'] = data['Calories']
                    lunch = pd.DataFrame(Lunchfoodseparated)
                    lunch['Calories'] = data['Calories']
                    dinner = pd.DataFrame(Dinnerfoodseparated)
                    dinner['Calories'] = data['Calories']

                    #Creating a suitable diet
                    current_cal = 0
                    b_diet=[]
                    l_diet=[]
                    d_diet=[]
                    #breakfast
                    i = random.randint(0,41)
                    j = random.randint(0,44)
                    z = random.randint(0,60)
                    while current_cal <= req_calories:
                        b_diet.append(bfast[0][i])
                        l_diet.append(lunch[0][j])
                        d_diet.append(dinner[0][z])
                        current_cal = current_cal + bfast['Calories'][i] + lunch['Calories'][j] + dinner['Calories'][z]
                        i+=1
                        j+=1
                        z+=1
                        
                    #Breakfast
                    st.subheader("Breakfast")
                    for i in range(len(b_diet)):
                        st.write("-",b_diet[i])

                    #Lunch
                    st.subheader("Lunch")
                    for i in range(len(l_diet)):
                        st.write("-",l_diet[i])

                    #Dinner
                    st.subheader("Dinner")
                    for i in range(len(d_diet)):
                        st.write("-",d_diet[i])
                        
#funtion to check diabetes
def diabetes_checker(preg,glu,bp,sT,ins,bmi,dp,age):
    input = [preg,glu,bp,sT,ins,bmi,dp,age]
    prediction = catboost_model.predict(input)
    if prediction == 0:
        return "Not Diabetic"
    else:
        return "Diabetic"