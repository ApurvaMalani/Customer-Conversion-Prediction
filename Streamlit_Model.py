import xgboost as xgb
import streamlit as st
import pandas as pd
import joblib

#Loading up the Regression model we created
model = joblib.load('xgb_model.pkl')

# Define the prediction function
def pred(age, job, marital, education_qual, call_type, day, mon, dur, num_calls, prev_outcome):
    if job=='blue-collar':
        job=0
    elif job=='entrepreneur':
        job=1
    elif job=='housemaid':
        job=2
    elif job=='services':
        job=3
    elif job=='technician':
        job=4
    elif job=='self-employed':
        job=5
    elif job=='admin.':
        job=6
    elif job=='management':
        job=7
    elif job=='unemployed':
        job=8
    elif job=='retired':
        job=9
    elif job=='student':
        job=10
    elif job=='unknown':
        job=0

    if marital=='married':
        marital=0
    elif marital=='divorced':
        marital=1
    elif marital=='single':
        marital=2

    if education_qual=='primary':
        education_qual=0
    elif education_qual=='secondary' or education_qual=='unknown':
        education_qual=1
    elif education_qual=='tertiary':
        education_qual=2

    if call_type=='unknown':
        call_type=0
    elif call_type=='telephone':
        call_type=1
    elif call_type=='cellular':
        call_type=2

    if mon=='may':
        mon=0
    elif mon=='jul':
        mon=1
    elif mon=='jan':
        mon=2
    elif mon=='nov':
        mon=3
    elif mon=='jun':
        mon=4
    elif mon=='aug':
        mon=5
    elif mon=='feb':
        mon=6
    elif mon=='apr':
        mon=7
    elif mon=='oct':
        mon=8
    elif mon=='sep':
        mon=9
    elif mon=='dec':
        mon=10
    elif mon=='mar':
        mon=11

    if prev_outcome=='unknown':
        prev_outcome=0
    elif prev_outcome=='failure':
        prev_outcome=1
    elif prev_outcome=='other':
        prev_outcome=2
    elif prev_outcome=='success':
        prev_outcome=3

    if num_calls>6:
        num_calls=6

    prediction= model.predict([[age, job, marital, education_qual, call_type, day, mon, dur, num_calls, prev_outcome]])
    print(prediction)

    return abs(prediction)
   
st.title('Customer Conversion Predictor')
# st.image()
st.header('Enter the characteristics of the Potential Customer:')

age= st.number_input("Age of the person : ", min_value=0, max_value=100, value=20)
job = st.selectbox("Customer's Job : ", ['management', 'technician', 'entrepreneur', 'blue-collar', 'unknown', 'retired',
                                         'admin.', 'services', 'self-employed', 'unemployed', 'housemaid', 'student'])
marital = st.selectbox("Customer's Marital Status :", ['married', 'single', 'divorced'])
education_qual = st.selectbox("Customer's Educational Status :", ['tertiary', 'secondary', 'unknown', 'primary'])
call_type = st.selectbox("Type of call :", ['unknown', 'cellular', 'telephone'])
day = st.number_input("Day of call made (1 to 31) : ", min_value=1, max_value=31, value=1)
mon = st.selectbox("Month of contact :",['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
dur = st.number_input("Duration of call in secs:", min_value=0)
num_calls = st.number_input("Number of calls made :", min_value=0, value=0)
prev_outcome = st.selectbox("Previous outcome of contact :", ['unknown', 'failure', 'other', 'success'])

if st.button('Predict Outcome'):
    result= pred(age, job, marital, education_qual, call_type, day, mon, dur, num_calls, prev_outcome)
    if (result[0])==1:
        st.success("The Customer is likely to get converted successfully.")
    else:
        st.warning("The Customer is unlikely to get converted.")
