#Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#load the model from disk
import joblib
model = joblib.load(r"C:\Users\raviv\OneDrive\Documents\learning\Youtube\Customer_Churn_Prediction\saved_models\model.sav")



def main():
    #Setting Application title
    st.title('Telco Customer Churn Prediction App')

      #Setting Application description
    st.markdown("""
     :dart:  This Streamlit app is made to predict customer churn in a ficitional telecommunication use case.
    The application is functional for both online prediction and batch data prediction. n
    """)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    #Setting Application sidebar default
    image = Image.open(r'C:\Users\raviv\OneDrive\Documents\learning\Youtube\Customer_Churn_Prediction\Images\churn_prediction_app.png')
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?", ("Online", "Batch"))
    st.sidebar.info('This app is created to predict Customer Churn')
    st.sidebar.image(image)

    if add_selectbox == "Online":
        st.info("Input data below")
        
        # Input fields based on your dataset features
        st.subheader("Customer Information")
        
        credit_score = st.number_input('Credit Score:', min_value=0, max_value=1000, value=600)
        geography = st.selectbox('Geography:', ('France', 'Germany', 'Spain'))
        gender = st.selectbox('Gender:', ('Female', 'Male'))
        age = st.slider('Age:', min_value=18, max_value=100, value=30)
        
        st.subheader("Customer Account Information")
        
        tenure = st.slider('Number of years the customer has stayed with the bank:', min_value=0, max_value=10, value=0)
        balance = st.number_input('Account Balance:', min_value=0.00, max_value=300000.00, value=0.00)
        num_of_products = st.selectbox('Number of Products:', (1, 2, 3, 4))
        has_credit_card = st.selectbox('Has Credit Card:', ('Yes', 'No'))
        is_active_member = st.selectbox('Is Active Member:', ('Yes', 'No'))
        estimated_salary = st.number_input('Estimated Salary:', min_value=0.00, max_value=200000.00, value=0.00)
        
        # st.subheader("Churn Information")
        
        # exited = st.selectbox('Exited (Churned):', ('Yes', 'No'))
        
        # Map input values to corresponding numeric codes
        data = {
            'CreditScore': credit_score,
            'Geography': {'France': 0, 'Germany': 1, 'Spain': 2}[geography],
            'Gender': 0 if gender == 'Female' else 1,
            'Age': age,
            'Tenure': tenure,
            'Balance': balance,
            'NumOfProducts': num_of_products,
            'HasCrCard': 1 if has_credit_card == 'Yes' else 0,
            'IsActiveMember': 1 if is_active_member == 'Yes' else 0,
            'EstimatedSalary': estimated_salary
            # 'Exited': 1 if exited == 'Yes' else 0  # Normally used only for labels, not inputs
        }
        
        # Convert the data into a DataFrame (in the format expected by your model)
        input_df = pd.DataFrame([data])
        
        # Display the input overview
        st.markdown("<h3>Overview of Input Data</h3>", unsafe_allow_html=True)
        st.dataframe(input_df)
        
        # Predict using your trained model
        prediction = model.predict(input_df)
        
        if st.button('Predict'):
            if prediction[0] == 1:
                st.warning('Yes, the customer will terminate the service.')
            else:
                st.success('No, the customer is happy with the services.')


        # data = {
        #         'SeniorCitizen': seniorcitizen,
        #         'Dependents': dependents,
        #         'tenure':tenure,
        #         'PhoneService': phoneservice,
        #         'MultipleLines': mutliplelines,
        #         'InternetService': internetservice,
        #         'OnlineSecurity': onlinesecurity,
        #         'OnlineBackup': onlinebackup,
        #         'TechSupport': techsupport,
        #         'StreamingTV': streamingtv,
        #         'StreamingMovies': streamingmovies,
        #         'Contract': contract,
        #         'PaperlessBilling': paperlessbilling,
        #         'PaymentMethod':PaymentMethod,
        #         'MonthlyCharges': monthlycharges,
        #         'TotalCharges': totalcharges
        #         }
        # features_df = pd.DataFrame.from_dict([data])
        # st.markdown("<h3></h3>", unsafe_allow_html=True)
        # st.write('Overview of input is shown below')
        # st.markdown("<h3></h3>", unsafe_allow_html=True)
        # st.dataframe(features_df)
        # #Preprocess inputs
        # preprocess_df = preprocess(features_df, 'Online')

        # prediction = model.predict(preprocess_df)

        # if st.button('Predict'):
        #     if prediction == 1:
        #         st.warning('Yes, the customer will terminate the service.')
        #     else:
        #         st.success('No, the customer is happy with Telco Services.')


    else:
        pass
if __name__ == '__main__':
        main()