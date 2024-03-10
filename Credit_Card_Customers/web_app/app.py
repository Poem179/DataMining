import pandas as pd
import streamlit as st
import pickle
from sklearn.preprocessing import LabelEncoder


st.write('''
# Model Logistic_Regression

## Form prediction customers 
''')

col1, col2 = st.columns(2)

with col1:

    Customer_Age = st.slider('Customer_Age:', value=45, min_value=1, max_value=120)

    Gender = st.radio('Gender:', options=['M (Male)','F (Female)'])

    Dependent_count = st.number_input('Dependent_count:', value=3, min_value=0, max_value=20)

    Education_Level = st.selectbox('Education_Level:', index=0, options=['High School', 'Graduate', 'Uneducated', 'College', 'Post-Graduate', 'Doctorate', 'Unknown'])

    Marital_Status = st.selectbox('Marital_Status:', index=0, options=['Married', 'Single', 'Divorced', 'Unknown'])

    Income_Category = st.select_slider('Income_Category', value='$60K - $80K', options=['Less than $40K', '$40K - $60K', '$60K - $80K', '$80K - $120K', '$120K +', 'Unknown'])

    Card_Category = st.selectbox('Card_Category', index=0, options=['Blue', 'Gold', 'Silver', 'Platinum'])

    Months_on_book = st.number_input('Months_on_book', value=39, min_value=0, max_value=100)

    Total_Relationship_Count = st.number_input('Total_Relationship_Count', value=5, min_value=0, max_value=10)

with col2:
    Months_Inactive_12_mon = st.number_input('Months_Inactive_12_mon', value=1, min_value=0, max_value=12)

    Contacts_Count_12_mon = st.number_input('Contacts_Count_12_mon', value=3, min_value=0, max_value=10)

    Credit_Limit = st.number_input('Credit_Limit', value=12691, min_value=0)

    Total_Revolving_Bal = st.number_input('Total_Revolving_Bal', value=777, min_value=0)

    Avg_Open_To_Buy = st.number_input('Avg_Open_To_Buy', value=11914, min_value=0)

    Total_Amt_Chng_Q4_Q1 = st.number_input('Total_Amt_Chng_Q4_Q1', value=1.335, min_value=0.0)

    Total_Trans_Amt = st.number_input('Total_Trans_Amt', value=1144, min_value=0)

    Total_Trans_Ct = st.number_input('Total_Trans_Ct', value=42, min_value=0)

    Total_Ct_Chng_Q4_Q1 = st.number_input('Total_Ct_Chng_Q4_Q1', value=1.625, min_value=0.0)

    Avg_Utilization_Ratio = st.number_input('Avg_Utilization_Ratio', value=0.061, min_value=0.0)


def predict_Attrition_Flag(
    Customer_Age,
    Gender,
    Dependent_count,
    Education_Level,
    Marital_Status,
    Income_Category,
    Card_Category,
    Months_on_book,
    Total_Relationship_Count,
    Months_Inactive_12_mon,
    Contacts_Count_12_mon,
    Credit_Limit,
    Total_Revolving_Bal,
    Avg_Open_To_Buy,
    Total_Amt_Chng_Q4_Q1,
    Total_Trans_Amt,
    Total_Trans_Ct,
    Total_Ct_Chng_Q4_Q1,
    Avg_Utilization_Ratio):

    new_sample = pd.DataFrame({
        "Customer_Age": [Customer_Age],
        "Gender": Gender,
        "Dependent_count": [Dependent_count],
        "Education_Level": Education_Level,
        "Marital_Status": Marital_Status,
        "Income_Category": Income_Category,
        "Card_Category": Card_Category,
        "Months_on_book": [Months_on_book],
        "Total_Relationship_Count": [Total_Relationship_Count],
        "Months_Inactive_12_mon": [Months_Inactive_12_mon],
        "Contacts_Count_12_mon": [Contacts_Count_12_mon],
        "Credit_Limit": [Credit_Limit],
        "Total_Revolving_Bal": [Total_Revolving_Bal],
        "Avg_Open_To_Buy": [Avg_Open_To_Buy],
        "Total_Amt_Chng_Q4_Q1": [Total_Amt_Chng_Q4_Q1],
        "Total_Trans_Amt": [Total_Trans_Amt],
        "Total_Trans_Ct": [Total_Trans_Ct],
        "Total_Ct_Chng_Q4_Q1": [Total_Ct_Chng_Q4_Q1],
        "Avg_Utilization_Ratio": [Avg_Utilization_Ratio],
    })


    x = pd.DataFrame(new_sample)

    with open('Credit_Card_Customers/web_app/log_reg_CreditCardCustomers.pkl', 'rb') as f:
        __log_reg = pickle.load(f)

    predict = str(__log_reg.predict(x)[0])

    # if predict == "0":
    #     result = "Existing Customer"
    # else:
    #     result = "Attrited Customer"
    return predict

if st.button('Compute a prediction'):

    gender = LabelEncoder()
    Gender = gender.fit_transform([Gender])

    marital = LabelEncoder()
    Marital_Status = marital.fit_transform([Marital_Status])

    card = LabelEncoder()
    Card_Category = card.fit_transform([Card_Category])

    edu = LabelEncoder()
    Education_Level = edu.fit_transform([Education_Level])

    income = LabelEncoder()
    Income_Category = income.fit_transform([Income_Category])

    predict = predict_Attrition_Flag(
                    Customer_Age,
                    Gender,
                    Dependent_count,
                    Education_Level,
                    Marital_Status,
                    Income_Category,
                    Card_Category,
                    Months_on_book,
                    Total_Relationship_Count,
                    Months_Inactive_12_mon,
                    Contacts_Count_12_mon,
                    Credit_Limit,
                    Total_Revolving_Bal,
                    Avg_Open_To_Buy,
                    Total_Amt_Chng_Q4_Q1,
                    Total_Trans_Amt,
                    Total_Trans_Ct,
                    Total_Ct_Chng_Q4_Q1,
                    Avg_Utilization_Ratio,)

    st.success('Done')

    if predict == '0':
        st.write('Existing Customer')
    else:
        st.write('Attrited Customer')

