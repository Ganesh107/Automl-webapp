import pandas as pd
import numpy as np
import random

data = pd.read_csv('/home/user/Desktop/autoML-webapp/data/input.csv')
Breakfastdata=data['Breakfast'] 
BreakfastdataNumpy=Breakfastdata.to_numpy()

Lunchdata=data['Lunch']
LunchdataNumpy=Lunchdata.to_numpy()
    
Dinnerdata=data['Dinner']
DinnerdataNumpy=Dinnerdata.to_numpy()
    
Food_itemsdata=data['Food_items']
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

#Calculating BMR
weight = float(input("Enter the weight "))
height = float(input("Enter the height "))
age = float(input("Enter the age "))
bmr = (10*weight)+(6.25*height)-(5*age)-161
print("BMR = ",bmr)

#Calculating required calories
print("Enter exercise rate [no,light,moderate,hard]")
exercise_rate = input("Enter exercise rate ")
if exercise_rate == "no":
    req_calories = bmr*1.2
elif exercise_rate == "light":
    req_calories = bmr*1.375
elif exercise_rate == "moderate":
    req_calories = bmr*1.725
elif exercise_rate == "hard":
    req_calories = bmr*1.9
else:
    print("Invalid Input")
print('req_cal = ' ,req_calories)

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

print("Diet Plan")
print("------------------------------------------")
#Breakfast
print("Breakfast")
print(b_diet)

#Lunch
print("Lunch")
print(l_diet)

#Dinner
print("Dinner")
print(d_diet)
