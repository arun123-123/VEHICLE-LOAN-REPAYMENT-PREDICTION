import streamlit as st
import pandas as pd
import pickle
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image
with open("VehicleLoan_Classification_Model_AFHP.pkl","rb") as f1:
    class_model_afhp= pickle.load(f1)

st.set_page_config(layout="wide")
st.title(":blue[**NBFI Vehicle Loan Repayment**]")
st.write("")
with st.sidebar:
    select= option_menu("MAIN MENU",["Home", "Loan Repayment Prediction"])
if select == "Home":
     st.subheader(":rainbow[**A non-banking financial institution (NBFI) or non-bank financial company (NBFC) is a type of financial institution that is not authorized to operate as a bank or is not under the supervision of a banking regulatory agency at the national or international level. NBFCs provide financial services similar to those of banks, such as investment, risk pooling, contractual savings, and market brokering.**]")
     st.subheader(":green[**Application predicts whether the client is default on loan payment or not**]")
     img= Image.open(r"C:\Users\HP\Downloads\Commercial Vehicle Loan in Meerut _ For more details contact us at +91-8630683568.jpg")
     img1= Image.open(r"C:\Users\HP\Downloads\House Loan Vectors & Illustrations for Free Download _ Freepik.jpg")
     col1, col2 = st.columns(2)
     with col1:
       st.image(img, width=500)
     with col2:
         st.write("")
         st.image(img1, width=600)
elif select== "Loan Repayment Prediction":
    def run():
        #st.title("NBFI Prediction using Machine Learning")
        Client_Income = st.number_input('Client_Income')
        Car_Owned = st.number_input('Car_Owned')
        Bike_Owned=st.number_input('Bike_Owned')
        Active_Loan=st.number_input('Active_Loan')
        House_Own=st.number_input('House_Own')
        Child_Count=st.number_input('Child_Count')
        Credit_Amount=st.number_input('Credit_Amount')
        Loan_Annuity=st.number_input('Loan_Annuity')
        
        Accompany_Client=([1, 6, 4, 3, 5, 0, 2])
        acc=st.selectbox('Accompany_Client',Accompany_Client)
        
        Client_Income_Type=([1, 5, 4, 2, 6, 7, 3, 0])
        cit=st.selectbox("Client_Income_Type",Client_Income_Type)
        
        Client_Education=([4, 0, 1, 2, 3])
        ce= st.selectbox("Client_Education",Client_Education)
        
        Client_Marital_Status =([1, 3, 2,0])
        cms=st.selectbox("Client_Marital_status",Client_Marital_Status)
        
        Client_Gender=([1, 0, 2])
        cg=st.selectbox("Client_Gender",Client_Gender)
        
        Loan_Contract_Type=([0, 1])
        lct= st.selectbox("Loan_Contract_Type",Loan_Contract_Type)
        
        Client_Housing_Type=([1, 0, 3, 2, 4, 5])
        ht=st.selectbox('Client_Housing_Type',Client_Housing_Type)
        
        Population_Region_Relative=st.number_input('Population_Region_Relative')
        Age_Days=st.number_input('Age_Days')
        Employed_Days=st.number_input('Employed_Days')
        Registration_Days=st.number_input('Registration_Days')
        ID_Days=st.number_input('ID_Days')
        #Own_House_Age=st.text_input('Own_House_Age')
        Mobile_Tag=st.number_input('Mobile_Tag')
        Homephone_Tag=st.number_input('Homephone_Tag')
        Workphone_Working=st.number_input('Workphone_Working')
        
        Client_Occupation=([14,  8, 13,  3,  4, 10,  0,  6,  1,  5, 17,  9, 11,  2, 12, 16,  7,
        15])
        co=st.selectbox('Client_occupation',Client_Occupation)
        
        Client_Family_Members=st.number_input('Client_Family_Members')
        Cleint_City_Rating=st.number_input('Cleint_City_Rating')
        Application_Process_Day=st.number_input('Application_Process_Day')
        Application_Process_Hour=st.number_input('Application_Process_Hour')
        Client_Permanent_Match_Tag=([1, 0])
        cpmt=st.selectbox('Client_Permanent_Match_Tag',Client_Permanent_Match_Tag)
        Client_Contact_Work_Tag=([1, 0])
        ccwt=st.selectbox('Client_Contact_Work_Tag',Client_Contact_Work_Tag)
        
        #Client_Contact_Work_Tag=st.number_input('Client_Contact_Work_Tag')
        Type_Organization=([42, 11, 57,  5, 33, 20,  4,  3, 55,  7, 28, 47, 19, 51, 46,  1, 31,
        30, 13, 14, 16,  2, 39, 26, 35, 56, 53, 38,  9, 34, 21, 41, 43, 54,
        32, 12, 40, 24,  0,  6, 36, 50,  8, 22, 44, 45, 17, 25, 27, 10, 29,
        15, 48, 23, 52, 18, 37, 49])
        to=st.selectbox('Type_organization',Type_Organization)
        #Score_Source_1=st.text_input('Score_Source_1')
        Score_Source_2=st.number_input('Score_Source_2')
        Score_Source_3=st.number_input('Score_Source_3')
        #Social_Circle_Default=st.text_input('Social_Circle_Default')
        Phone_Change=st.number_input('Phone_Change')
        Credit_Bureau=st.number_input('Credit_Bureau')
        st.write("")
        if st.button("Submit"):
            user_input=pd.DataFrame({'Client_Income':[Client_Income],
                               'Car_Owned':[Car_Owned],
                               'Bike_Owned':[Bike_Owned],
                               'Active_Loan':[Active_Loan],
                               'House_Own':[House_Own],
                               'Child_Count':[Child_Count],
                               'Credit_Amount':Credit_Amount,
                               'Loan_Annuity':[Loan_Annuity],
                               'Accompany_Client':[acc],
                               'Client_Income_Type':[cit],
                               'Client_Education':[ce],
                               'Client_Marital_Status':[cms],
                               'Client_Gender':[cg],
                               'Loan_Contract_Type':[lct],
                               'Client_Housing_Type':[ht],
                               'Population_Region_Relative':[Population_Region_Relative],
                               'Age_Days':[Age_Days],
                               'Employed_Days':[Employed_Days],
                               'Registration_Days':[Registration_Days],
                               'ID_Days':[ID_Days],
                               #'Own_House_Age':[Own_House_Age],
                               'Mobile_Tag':[Mobile_Tag],
                               'Homephone_Tag':[Homephone_Tag],
                               'Workphone_Working':[Workphone_Working],
                               'Client_Occupation':[co],
                               'Client_Family_Members':[Client_Family_Members],
                               'Cleint_City_Rating':[Cleint_City_Rating],
                               'Application_Process_Day':[Application_Process_Day],
                               'Application_Process_Hour':[Application_Process_Hour],
                               'Client_Permanent_Match_Tag':[cpmt],
                               'Client_Contact_Work_Tag':[ccwt],
                               'Type_Organization':[to],
                               #'Score_Source_1':[Score_Source_1],
                                'Score_Source_2':[Score_Source_2],
                                'Score_Source_3':[Score_Source_3],
                               #'Social_Circle_Default':[Social_Circle_Default],
                               'Phone_Change':[Phone_Change],
                               'Credit_Bureau':[Credit_Bureau]})
            st.write(user_input)
            y_p=class_model_afhp.predict(user_input)
            st.write("")
            if(y_p==1):
              st.write(":red[**Default**]")
            else:
              st.write(":green[**No Default**]")
    run()
