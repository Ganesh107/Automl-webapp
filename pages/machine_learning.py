import numpy
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import seaborn as sns

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
            params = add_parameters(model_name)
            model = build_model(model_name,params)
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            st.write("Model = ",model_name)
            st.write("Accuracy = ",accuracy_score(y_test,y_pred))
            mat = confusion_matrix(y_test, y_pred)
            st.write(sns.heatmap(mat,annot=True))
            st.pyplot()
            st.set_option('deprecation.showPyplotGlobalUse', False)

#function to add parameters
def add_parameters(clf_name):
    params = dict()
    if clf_name == "KNN":
        k = st.sidebar.slider("K",1,10)
        params['k'] = k   
    elif clf_name == "SVM":
        c = st.sidebar.slider("C",0.01,5.0) 
        gamma = st.sidebar.slider("gamma",0.001,3.0)
        params['c'] = c
        params['gamma'] = gamma
    else:
        max_depth = st.sidebar.slider("max depth",2,15)
        max_samples = st.sidebar.slider("max_samples",1,500,step=10)
        params['max_depth'] = max_depth
        params['max_samples'] = max_samples
    return params

#function to build various ml models
def build_model(model_name,params):
    if model_name == "KNN":
        model = KNeighborsClassifier(n_neighbors=params['k'])
    elif model_name == "SVM":
        model = SVC(C=params['c'],gamma=params['gamma'])
    else:
        model = RandomForestClassifier(max_depth=params['max_depth'],max_samples=params['max_samples'])
    return model