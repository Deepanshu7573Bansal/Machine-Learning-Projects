# import library
import streamlit as st
import pickle
import pandas as pd

# Pickle file Salary
Salary = pickle.load(open('Salary.pkl','rb'))

# function prediction
def prediction(Education,j,gender,exp):
    exp_l=[]
    exp_g=[]
    for i in range(Salary.shape[0]+1):
        if i!=172 and i!=260:
            if edu[i]==Education and job[i]==str(j) and gen[i]==gender:
                if yeo[i]<exp:
                    exp_l.append(s[i])
                elif yeo[i]>exp:
                    exp_g.append(s[i])
                elif yeo[i]==exp:
                    return s[i]
    if len(exp_l) == 0 and len(exp_g) != 0:
        exp_g.sort()
        return exp_g[0] / 2
    if len(exp_l) != 0 and len(exp_g) == 0:
        return sum(exp_l) / len(exp_l)
    if len(exp_l) == 0 and len(exp_g) == 0:
        return "No such job found."
    less = sum(exp_l)/len(exp_l)
    great = sum(exp_g)/len(exp_g)
    return (less+great)/2

# Print text
st.header("Salary prediction system")
st.write("In this prediction model mainly work on predict salary by given some input data.")


Select_education = st.selectbox(
    "Select your education level",
    Salary['Education Level'].unique()
)
Select_job = st.selectbox(
    "Select your job title",
    Salary['Job Title'].unique()
)
Select_gender = st.selectbox(
    "Select your gender",
    Salary['Gender'].unique()
)
experience = st.number_input("Enter experience")
if st.button('Check salary'):
    edu = Salary['Education Level']
    job = Salary['Job Title']
    gen = Salary['Gender']
    yeo = Salary['Years of Experience']
    s = Salary['Salary']
    st.text('Predicted salary:')
    st.text(prediction(Select_education,Select_job,Select_gender,experience))
