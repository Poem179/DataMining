import pickle
import json
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

__log_reg = None
__card = None
__edu = None
__gender = None
__income = None 
__marital = None 
__columns = None
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
    
    # try:
    #     loc_index = __card.index(Card_Category.lower())
    # except:
    #     loc_index = -1
    #
    # if loc_index == 0:
    #     Card_Category = 0
    # elif loc_index == 1:
    #     Card_Category = 1
    # elif loc_index == 2:
    #     Card_Category = 2
    # elif loc_index == 3:
    #     Card_Category = 3
    # elif loc_index == 4:
    #     Card_Category = 4
    # elif loc_index == 5:
    #     Card_Category = 5
    #
    #
    # try:
    #     loc_index1 = __edu.index(Education_Level.lower())
    # except:
    #     loc_index1 = -1
    #
    # if loc_index1 == 0:
    #     Education_Level = 0
    # elif loc_index1 == 1:
    #     Education_Level = 1
    # elif loc_index1 == 2:
    #     Education_Level = 2
    # elif loc_index1 == 3:
    #     Education_Level = 3
    # elif loc_index1 == 4:
    #     Education_Level = 4
    # elif loc_index1 == 5:
    #     Education_Level = 5
    # elif loc_index1 == 6:
    #     Education_Level = 6
    #
    #
    # try:
    #     loc_index2 = __income.index(Income_Category.lower())
    # except:
    #     loc_index2 = -1
    #
    # if loc_index2 == 0:
    #     Income_Category = 0
    # elif loc_index2 == 1:
    #     Income_Category = 1
    # elif loc_index2 == 2:
    #     Income_Category = 2
    # elif loc_index2 == 3:
    #     Income_Category = 3
    #
    # try:
    #     loc_index3 = __marital.index(Marital_Status.lower())
    # except:
    #     loc_index3 = -1
    #
    # if loc_index3 == 0:
    #     Marital_Status = 0
    # elif loc_index3 == 1:
    #     Marital_Status = 1
    # elif loc_index3 == 2:
    #     Marital_Status = 2
    # elif loc_index3 == 3:
    #     Marital_Status = 3
    #
    #
    # try:
    #     loc_index4 = __gender.index(Gender.lower())
    # except:
    #     loc_index4 = -1
    #
    # if loc_index4 == 0:
    #     Gender = 0
    # elif loc_index4 == 1:
    #     Gender = 1


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



    # new_sample = [[
    #                 Customer_Age,
    #                 Gender,
    #                 Dependent_count,
    #                 Education_Level,
    #                 Marital_Status,
    #                 Income_Category,
    #                 Card_Category,
    #                 Months_on_book,
    #                 Total_Relationship_Count,
    #                 Months_Inactive_12_mon,
    #                 Contacts_Count_12_mon,
    #                 Credit_Limit,
    #                 Total_Revolving_Bal,
    #                 Avg_Open_To_Buy,
    #                 Total_Amt_Chng_Q4_Q1,
    #                 Total_Trans_Amt,
    #                 Total_Trans_Ct,
    #                 Total_Ct_Chng_Q4_Q1,
    #                 Avg_Utilization_Ratio,
    # ]]

    x = pd.DataFrame(new_sample)
    x.columns = __columns


    predict = str(__log_reg.predict(x)[0])
        
    if predict == "0":
        result = "Existing Customer"
    else:
        result = "Attrited Customer"
    return result

def load_saved_artifacts():
    print("Loading saved arrtifact...starting")
    global __card
    global __edu
    global __income
    global __marital
    global __gender
    global __columns
    with open("./artifacts/edu_value.json", "r") as f:
        __edu = json.load(f)['edu_value']
    with open("./artifacts/income_value.json", "r") as f:
        __income = json.load(f)['income_value']
    with open("./artifacts/marital_value.json", "r") as f:
        __marital = json.load(f)['marital_value']
    with open("./artifacts/gender_value.json", "r") as f:
        __gender = json.load(f)['gender_value']
    with open("./artifacts/card_value.json", "r") as f:
        __card = json.load(f)['card_value']
    with open("artifacts/columns.json", "r") as f:
        __columns = json.load(f)['columms']
    
    
    global __log_reg
    if __log_reg is None:
        with open('./artifacts/log_reg_CreditCardCustomers.pkl', 'rb') as f:
            __log_reg = pickle.load(f)
    print("Laoding saved articfacts...done")
    
def get_card():
    return __card
    
def get_edu():
    return __edu

def get_gender():
    return __gender

def get_income():
    return __income

def get_marital():
    return __marital

def get_columns():
    return __columns

if __name__ == '__main__':
    load_saved_artifacts()
    