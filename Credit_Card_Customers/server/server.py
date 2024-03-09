from flask import Flask, jsonify, request
#import os
#from flask_restful import Resource, Api
#import os, sys
#from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import util
app = Flask(__name__)
# app = Flask(__name__)
# api = Api(app)

# class HelloWord(Resource):
#     def get(self):
#         return{"message": "Hello Word"}
    
# api.add_resource(HelloWord, '/')

# if __name__ == '__main__':
#     parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
#     parser.add_argument("-post", type=str, default="1412", help="post")
#     args = vars(parser.parse_args())
#     app_post = args["post"]
#     app.run(debug=True, host='0.0.0.0', port=app_post)



@app.route('/get_artifacts', methods=['GET'])
def get_location_names():
    response = jsonify({
        'edu': util.get_edu(),
        'gender': util.get_gender(),
        'income': util.get_income(),
        'marital': util.get_marital(),
        'card': util.get_card(),
        'columns': util.get_columns()
    })
    
    response.headers.add('Access-Control-Allow_Origin', '*')
    
    return response 

@app.route('/predict_Attrition_Flag', methods=['GET', 'POST'])
def predict():
    Customer_Age= int(request.form['Customer_Age'])
    Gender = request.form['Gender']
    Dependent_count= int(request.form['Dependent_count'])
    Education_Level= request.form['Education_Level']
    Marital_Status= request.form['Marital_Status']
    Income_Category= request.form['Income_Category']
    Card_Category= request.form['Card_Category']
    Months_on_book= int(request.form['Months_on_book'])
    Total_Relationship_Count= int(request.form['Total_Relationship_Count'])
    Months_Inactive_12_mon= int(request.form['Months_Inactive_12_mon'])
    Contacts_Count_12_mon= int(request.form['Contacts_Count_12_mon'])
    Credit_Limit= float(request.form['Credit_Limit'])
    Total_Revolving_Bal= int(request.form['Total_Revolving_Bal'])
    Avg_Open_To_Buy= float(request.form['Avg_Open_To_Buy'])
    Total_Amt_Chng_Q4_Q1= float(request.form['Total_Amt_Chng_Q4_Q1'])
    Total_Trans_Amt= int(request.form['Total_Trans_Amt'])
    Total_Trans_Ct= int(request.form['Total_Trans_Ct'])
    Total_Ct_Chng_Q4_Q1= float(request.form['Total_Ct_Chng_Q4_Q1'])
    Avg_Utilization_Ratio= float(request.form['Avg_Utilization_Ratio'])
    
    response = jsonify({
        'predict_Attrition_Flag': util.predict_Attrition_Flag(
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
            Avg_Utilization_Ratio)
    })

    response.headers.add('Access-Control-Allow_Origin', '*')
    
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Prediction...")
    util.load_saved_artifacts()
    app.run()