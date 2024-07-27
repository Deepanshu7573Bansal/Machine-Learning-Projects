# import libraries
import streamlit as st
import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier

# import pickle file
df = pickle.load(open('iris.pkl','rb'))

# prediction function
def prediction(SL,SW,PL,PW):
    X = df.iloc[:, 0:-1]
    Y = df.iloc[:, -1]
    KNN = KNeighborsClassifier(n_neighbors=5)
    KNN.fit(X, Y)
    y_pred = KNN.predict([[SL,SW,PL,PW]])
    y_pred = pd.DataFrame(y_pred)
    print(y_pred)
    if y_pred[0].values==0:
        return 'Iris-setosa'
    elif y_pred[0].values==1:
        return 'Iris-versicolor'
    elif y_pred[0].values==2:
        return 'Iris-virginica'


# Heading and text
st.header("Iris dataset model")

# Take input
SL = st.number_input("Enter sepal length")
SW = st.number_input("Enter sepal width")
PL = st.number_input("Enter petal length")
PW = st.number_input("Enter petal width")

# button for check specie
if st.button('Check specie'):
    st.text("Specie:")
    st.text(prediction(SL,SW,PL,PW))
