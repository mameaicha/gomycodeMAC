# 1. Import the necessary libraries: Streamlit, sklearn.datasets, and sklearn.ensemble.

import streamlit as st
import pandas as pd
import numpy as np
import sklearn.datasets as datasets 
import sklearn.ensemble
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
# supervised learning
from sklearn.ensemble import RandomForestClassifier
#from sklearn import metrics
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, f1_score,roc_auc_score, roc_curve,classification_report
import time

# 2.Load the iris dataset using the "datasets.load_iris()" function and assign the data and target variables to "X" and "Y", respectively.

data= datasets.load_iris()
X=data.data
Y=data.target

# 3. # Set up a Random Forest Classifier and fit the model using the "RandomForestClassifier()" and "fit()" functions.

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 101)
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


rf_model = RandomForestClassifier(max_depth=4, max_features='auto', n_estimators=10,random_state=42)
rf_model.fit(x_train,y_train)


# 4. Create a Streamlit app using the "streamlit.title()" and "streamlit.header()" functions to add a title and header to the app

st.title("Iris Flower Prediction App")
st.subheader("Auteur: Mame Aïssatou CONTE")
st.markdown("this is a Streamlit application that  predicts the type of Iris flower based on user input using a Random Forest Classifier")


# 5. Add input fields for sepal length, sepal width, petal length, and petal width using the "streamlit.slider()" function. 
# Use the minimum, maximum, and mean values of each feature as the arguments for the function.

# minimum, maximum, and mean values of each feature
st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.84)
    sepal_width = st.sidebar.slider('Sepal width',  2.0 , 4.4 , 3.06)
    petal_length = st.sidebar.slider('Petal length', 1.0 , 6.9 , 3.76)
    petal_width = st.sidebar.slider('Petal width', 0.1 , 2.5 , 1.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# 6. Define a prediction button using the "streamlit.button()" function that takes in the input values and uses the classifier to predict the type of iris flower
# creation du boutton predict qui retourne la prediction
if st.button("prediction"):
    prediction= rf_model.predict(df)
    prediction_proba = rf_model.predict_proba(df)
    
    # 7. Use the "streamlit.write()" function to display the predicted type of iris flower on the app.
    st.subheader('Class labels and their corresponding index number')
    st.write(data.target_names)

    st.subheader('Prediction')
    st.write(data.target_names[prediction])
    #st.write(prediction)

    st.subheader('Prediction Probability')
    st.write(prediction_proba)

    
    