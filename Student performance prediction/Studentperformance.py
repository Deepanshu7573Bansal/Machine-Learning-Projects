# Import libraries
import streamlit as st
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import VotingRegressor

# open Pickle file
student = pickle.load(open('Studentperformance.pkl','rb'))

# function studentperformance predict answer
def studentperformance(gender,race,education,test):
    X = student.iloc[:, 0:4]
    Y = student.iloc[:, -1]

    v1 = LinearRegression()
    v2 = DecisionTreeRegressor()
    v3 = RandomForestRegressor()

    v1.fit(X, Y)
    v2.fit(X, Y)
    v3.fit(X, Y)

    estimators = [('v1', v1), ('v2', v2), ('v3', v3)]
    VR = VotingRegressor(estimators)
    VR.fit(X, Y)
    ans = VR.predict([[gender,race,education,test]])
    return ans

# text
st.header("Student performance prediction")
st.text("Some points:")
st.text("Gender: 1-Male, 0-female")
st.text("race/ethnicity: 0-group A, 1-group B, 2-group C, 3-group D, 4-group E")
st.text("parental level of education: 0-associate's degree, 1-bachelor's degree, 2-high school, 3-master's degree, 4-some college, 5-some high school")
st.text("test preparation course: 0-completed, 1-none")

# Streamlit selectbox
st_gender = st.selectbox(
    "Select your gender",
    student['gender'].unique()
)
st_race = st.selectbox(
    "Select your race/ethnicity",
    student['race/ethnicity'].unique()
)
st_education = st.selectbox(
    "Select your parental level of education",
    student['parental level of education'].unique()
)
st_test = st.selectbox(
    "Select your test preparation course",
    student['test preparation course'].unique()
)

if st.button('Check performance'):
    answer = studentperformance(st_gender,st_race,st_education,st_test)
    st.text("Student performance:")
    st.text(answer)