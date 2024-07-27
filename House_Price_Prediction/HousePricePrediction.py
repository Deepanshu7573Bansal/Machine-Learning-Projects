# import libraries
import streamlit as st
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# import pickle file
df = pickle.load(open('df.pkl','rb'))

# function of prediction
def prediction(n1,n2,n3):
    X = df.iloc[:, 0:-1]
    Y = df.iloc[:, -1]
    PF = PolynomialFeatures(degree=3)
    X = PF.fit_transform(X)
    LR = LinearRegression()
    LR.fit(X, Y)
    Y_pred = PF.fit_transform([[n1,n2,n3]])
    y_pred = LR.predict(Y_pred)
    return y_pred

# Heading and text
st.header("House Price Prediction")

# Take input and call prediction function
Badroom = st.number_input("Enter number of badroom")
Bathroom = st.number_input("Enter number of bathroom")
Area = st.number_input("Enter area of house")
if st.button('Check price'):
    st.text("House price:")
    st.text(prediction(Area,Badroom,Bathroom))
