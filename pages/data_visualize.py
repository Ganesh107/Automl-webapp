import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title("Visualization")
    st.subheader("UPLOAD DATASET")
    uploaded_file = st.file_uploader("Upload a CSV file ")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        cols = data.columns.tolist()
        plot_types = st.selectbox("Select type of plot",["Area chart","hist","box","kde"])
        selected_cols = st.multiselect("Select columns to plot",cols)

        #visualization plots
        if st.checkbox("Corrrelation Plot"):
            st.write(sns.heatmap(data.corr(),annot=True))
            st.pyplot()

        if st.checkbox("Pie plot"):
            target = st.text_input("Enter Target class")
            if target in data.columns:
                st.success("Generating a Pie plot")
                st.write(data[target].value_counts().plot.pie(autopct="%1.1f%%"))
                st.pyplot()
            else:
                st.warning("Please enter correct column name")
                st.error("Invalid column name entered")

        #if st.button("Create Plot"):
        #   st.success("Creating {} for {}".format(plot_types,selected_cols))
        
        #Visualization - charts
        if plot_types == 'Area chart':
            cols_to_plot = data[selected_cols]
            st.area_chart(cols_to_plot)

        elif plot_types:
            st.set_option('deprecation.showPyplotGlobalUse', False)
            custom_plot = data[selected_cols].plot(kind=plot_types)
            st.write(custom_plot)
            st.pyplot()