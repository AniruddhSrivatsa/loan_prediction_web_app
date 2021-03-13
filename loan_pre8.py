#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pickle

st.header("Loan eligibility checker")
st.subheader("Gender :")
gender=st.selectbox("Select the gender",["Male","Female"])
if gender is not None:
  if gender=="Male":
    gender_int=1
  
  elif gender=="Female":
    gender_int=0
st.subheader("Married :")
Married=st.selectbox("Married or not",["Yes","No"])
if Married is not None:
  if Married=="Yes":
    marr_int=1
  
  elif Married=="No":
    marr_int=0

st.subheader("Eduaction :")
edu=st.selectbox("Graduated or not",["Graduated","Not Graduated"])
if edu is not None:
  if edu=="Graduated":
    edu_int=1
  
  elif edu=="Not Graduated":
    edu_int=0

st.subheader("No of Dependents :")
dep=st.selectbox("how many people are depending on you monetarily?",["0","1","2","3+"])
if dep is not None:
  if dep=="0":
    dep_int=0
  elif dep=="1":
    dep_int=1
  elif dep=="2":
    dep_int=2
  elif dep=="3+":
    dep_int=3

st.subheader("Self Employed ? :")
sem=st.selectbox("Self Employed or not",["Yes","No"])
if sem is not None:
  if sem=="Yes":
    sem_int=1
  
  elif sem=="No":
    sem_int=0

st.subheader("Applicant's income:")
app_inc=st.number_input("Applicant's income in dollars (per month)")/1000
st.subheader("Co-applicant's income :")
coapp_inc=st.number_input("Co-applicant's income in dollars (per month)")/1000
st.subheader("Loan Amount:")
loan_amt=st.number_input("Loan Amount in dollars")/1000

st.subheader("Loan Term (in no of yrs):")
loan_term=st.number_input("Term of loan (Duration)")

st.subheader("Property Area:")
dep=st.selectbox("which area are u living in ?",["Rural","Urban","Semiurban"])
if dep is not None:
  if dep=="Rural":
    loc_int=0
  elif dep=="Semiurban":
    loc_int=1
  elif dep=="Urban":
    loc_int=2
  

st.subheader("Credit History :")
st.write("whether u have pending loans or not")
cred_his=st.selectbox("pending_loans",["Yes","No"])
if cred_his is not None:
  if cred_his=="Yes":
    cred_int=0
  
  elif cred_his=="No":
    cred_int=1

ada_boost=pickle.load(open("ada.pkl","rb"))
par=[gender_int,marr_int,dep_int,edu_int,sem_int,app_inc,coapp_inc,loan_amt,loan_term,loc_int,cred_int]
result=["The loan is not granted","The loan is granted"]

st.sidebar.subheader("Additional Details")
reason=st.sidebar.radio("What is the reason for applying for loan ?",["Financial Problems","Education",
                                                             "House or other collateral buying",
                                                             "none of the above"])
if (reason=="none of the above"):
     reason1=st.sidebar.text_input("Enter the reason")

if st.checkbox("Predict"):
   pred=ada_boost.predict([par])
   if pred==1:
     st.write("Congratulations,",result[1])
     
   elif pred==0:
     st.write("Sorry,",result[0])
    
   
   

   if (pred==1 and reason !="none of the above"):
     st.write("We are happy to announce that your loan will be sanctioned for",reason)
     
    
   elif(pred==1 and reason=="none of the above"):
     st.markdown("""<style>.big-font {font-size:30px !important;}</style>""", unsafe_allow_html=True)

     st.markdown('<p class="big-font">We are happy to announce that your loan will be sanctioned.</p>', unsafe_allow_html=True)
    
     st.write(reason1)
    
   elif (pred==0 and reason !="none of the above"):
     st.write("We are happy to announce that your loan will be sanctioned for",reason)








# In[ ]:




