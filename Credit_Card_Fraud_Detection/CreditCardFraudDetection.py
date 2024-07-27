import streamlit as st
import pickle
from sklearn.ensemble import RandomForestClassifier

Data = pickle.load(open('CreditCardFraud.pkl','rb'))
Data1 = pickle.load(open('TestCreditCardFraud.pkl','rb'))

def function(amount,gender,city,state,zip,job,category):
    X = Data.iloc[:, :-1]
    Y = Data.iloc[:, -1]
    RF = RandomForestClassifier(n_estimators=50)
    RF.fit(X, Y)
    y_pred = RF.predict([[amount,gender,city,state,zip,job,category]])
    return y_pred

st.title("Credit Card Fraud Detection")
amount=st.number_input("Enter amount")
gender=st.selectbox(
    "Select gender",
    Data1['gender'].unique()
)
city=st.selectbox(
    "Select city",
    Data1['city'].unique()
)
state=st.selectbox(
    "Select state",
    Data1["state"].unique()
)
zip=st.selectbox(
    "Select zip",
    Data1["zip"].unique()
)
job=st.selectbox(
    "Select job",
    Data1["job"].unique()
)
category=st.selectbox(
    "Select category",
    Data1["category"].unique()
)

if st.button("Check credit card fraud"):
    for i in range(Data1['gender'].unique().shape[0]):
        if Data1['gender'].unique()[i]==gender:
            gender=Data['gender'].unique()[i]
            break

    for i in range(Data1['city'].unique().shape[0]):
        if Data1['city'].unique()[i]==city:
            city=Data['city'].unique()[i]
            break

    for i in range(Data1['state'].unique().shape[0]):
        if Data1['state'].unique()[i]==state:
            state=Data['state'].unique()[i]
            break

    for i in range(Data1['zip'].unique().shape[0]):
        if Data1['zip'].unique()[i]==zip:
            zip=Data['zip'].unique()[i]
            break

    for i in range(Data1['job'].unique().shape[0]):
        if Data1['job'].unique()[i]==job:
            job=Data['job'].unique()[i]
            break

    for i in range(Data1['category'].unique().shape[0]):
        if Data1['category'].unique()[i]==category:
            category=Data['category'].unique()[i]
            break

    if (function(amount,gender,city,state,zip,job,category))==0:
        st.text('Legitimate')
    else:
        st.text('Fraudulent')