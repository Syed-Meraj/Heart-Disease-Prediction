import streamlit as st
import pandas as pd 
import joblib 

st.title("Heart Disease Prediction")

gender=st.radio("Select Your Gender ",["Male","Female"])

if gender =="Male ":
    gender=1
else:
    gender=0 

age = st.slider("Select Your Age")

cigsPerDay = st.number_input("Enter No.of Ciggarettes Per Day")

BPMeds = st.radio("Do You Take BP medicines", ["True","False"])

if BPMeds=="True":
    BPMeds=1.0
else:
    BPMeds=0.0

prevstroke= st.radio("Do you have  any prevalent stroks ",["True","False"])


if prevstroke=="True":
    prevstroke=1
else:
    prevstroke=0

prevalentHyp=st.radio("Do you have  any prevalent hypertension ",["True","False"])


if prevalentHyp=="True":
    prevalentHyp=1
else:
    prevalentHyp=0

diabetes = st.radio("Do you have  Diabetes ",["True","False"])


if diabetes=="True":
    diabetes=1
else:
    diabetes=0

totChol = st.number_input("Enter your Cholestrol level ")

sysBP = st.number_input("Enter your systole blood pressure level")

diaBP = st.number_input("Enter your diastole blood pressure level")

bmi = st.number_input("Enter your BMI")

heart_rate = st.number_input("Enter your heart rate per min")

if st.button("prediction"):
    model = joblib.load("heart_model.h5")
    prediction =model.predict([[gender,age,cigsPerDay,BPMeds,prevstroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,bmi,heart_rate]])
    if prediction[0]== 0:
        prediction = "you are not at risk of getting a heart disease."
        st.success(prediction)
    else:
        pediction = "you are at risk of getting a heart disease."  
        st.success(prediction)   