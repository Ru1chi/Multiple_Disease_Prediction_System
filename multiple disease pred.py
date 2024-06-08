# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:39:59 2024

@author: sr322
"""

import pickle
import streamlit as st # type: ignore
from streamlit_option_menu import option_menu # type: ignore

#loading the saved models
diabetes_model=pickle.load(open('C:/Users/sr322/OneDrive/Desktop/ML_Model_Deployment/Multilpe_disease_prediction/diabetes_mode.sav','rb'))

hear_disease_model=pickle.load(open('C:/Users/sr322/OneDrive/Desktop/ML_Model_Deployment/Multilpe_disease_prediction/heart_disease_model.sav','rb'))
parkisons_disease_model=pickle.load(open('C:/Users/sr322/OneDrive/Desktop/ML_Model_Deployment/Multilpe_disease_prediction/parkinsons_model.sav','rb'))

#side bar for navigation

with st.sidebar:
    
    selected=option_menu('Multiple Disease Prediction System',
                         
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkisons Prediction'], 

                          icons=['activity','heart','person'],

                           default_index=0)
    
#diabetes prediction page

if(selected=='Diabetes Prediction'):

    #page title
    st.title('Diabetes Prediction using ML.')



#getting the input data from user
col1,col2,col3=st.columns(3)

with col1:
    Pregnancies=st.text_input("Number of Pregnencies-")

with col2:
    Glucose=st.text_input("Glucose level-")

with col3:
    BloodPressure=st.text_input("Blodd Pressure level-")

with col1:
    SkinThickness=st.text_input("Skinthikness level-")

with col2:
    Insulin=st.text_input("Insulin level-")

with col3:
    BMI=st.text_input("BMI rate is-")

with col1:
    DiabetesPedigreeFunction=st.text_input("DiabetesPedigreeFunction-")

with col2:
    Age=st.text_input("Age of the person-")


    #code for prediction

    diab_diognosis=''#create a wmpty string which stores the result

    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])#gives all this values to the model which we have loaded here
    
        if (diab_prediction[0]==1):
            diab_diognosis="The person is Diabetic."
        else:
            diab_diognosis="The person is not Diabetic."

    st.success(diab_diognosis)  #this will give us the diab_diognosis result     








#heart disease prediction page

if(selected=='Heart Disease Prediction'):

    #page title
    st.title('Heart Disease Prediction Using ML.')       


#getting the input data from user
col1,col2,col3=st.columns(3)

with col1:
    age=st.number_input("Age-")

with col2:
    sex=st.number_input("Sex-")

with col3:
    cp=st.number_input("Chest pain type(4 values)-")

with col1:
    trestbps=st.number_input("resting blood pressure-")

with col2:
    chol=st.number_input("serum cholestrol in mg/dl-")

with col3:
    fbs=st.number_input("fasting blood sugar>120m mg/dl-")

with col1:
    restecg=st.number_input("resting eclectrocardiographic results(values 0,1,2)-")

with col2:
    thalach=st.number_input("maximum heart rate achived-")

with col3:
    exang=st.number_input("exercise induced angina-")

with col1:
    oldpeak=st.number_input("oldpeak=ST depression induced by exercise relative to rest-")

with col2:
    slope=st.number_input("the slope of the peak exercise ST segment-")

with col3:
    ca=st.number_input("number of major vessels (0-3) colored by flourosopy-")

with col1:
    thal=st.number_input("thal:0=normal; 1=fixed defect;2=reversible defect-")





    #code for prediction

    heart_disease_diognosis=''#create a wmpty string which stores the result

    #creating a button for prediction
    if st.button('Heart Disease Test Result'):
        heart_disease_prediction=hear_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        #gives all this values to the model which we have loaded here
    
        if (heart_disease_prediction[0]==1):
            heart_disease_diognosis="The person has a heart disease."
        else:
            heart_disease_diognosis="The person does not have a heart disease."

    st.success(heart_disease_diognosis)  #this will give us the diab_diognosis result     






#parkison prediction page

if(selected=='Parkisons Prediction'):

    #page title
    st.title('Parkisons Prediction Using ML.')  


#getting the input data from user
col1,col2,col3,col4,col5=st.columns(5)

with col1:
    fo=st.number_input("MDVP:Fo(Hz)-")

with col2:
    fhi=st.number_input("MDVP:Fhi(Hz)-")

with col3:
    flo=st.number_input("MDVP:Flo(Hz)-")

with col4:
    Jitter_percent=st.number_input(" MDVP:Jitter(%)-")

with col5:
    Jitter_Abs=st.number_input(" MDVP:Jitter(Abs)-")

with col1:
    RAP=st.number_input("MDVP:RAP-")

with col2:
    PPQ=st.number_input("MDVP:PPQ-")

with col3:
    DDP=st.number_input(" Jitter:DDP-")

with col4:
    Shimmer=st.number_input("MDVP:Shimmer-")

with col5:
    Shimmer_dB=st.number_input(" MDVP:Shimmer(dB)-")

with col1:
    APQ3=st.number_input("Shimmer:APQ3-")

with col2:
    APQ5=st.number_input(" Shimmer:APQ5-")

with col3:
    APQ = st.text_input('MDVP:APQ')
        
with col4:
    DDA=st.number_input("Shimmer:DDA-")

with col5:
    NHR=st.number_input("  NHR-")

with col1:
    HNR=st.number_input("HNR-")

with col2:
    RPDE=st.number_input("RPDE-")

with col3:
    DFA=st.number_input(" DFA-")
    
with col4:
    spread1=st.number_input("spread1-")

    
with col5:
    spread2=st.number_input(" spread2-")
        
with col1:
    D2=st.number_input("D2-")
    
with col2:
    PPE=st.number_input("PE-")


    #code for prediction

    parkison_disease_diognosis=''#create a wmpty string which stores the result

    #creating a button for prediction
    if st.button('Parkison Disease Test Result'):
        parkison_disease_prediction=parkisons_disease_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        #gives all this values to the model which we have loaded here
    
        if (parkison_disease_prediction[0]==1):
            parkison_disease_diognosis="The person has parkisons."
        else:
            parkison_disease_diognosis="The person does nor have Parksons."

    st.success(parkison_disease_diognosis)  #this will give us the diab_diognosis result     


