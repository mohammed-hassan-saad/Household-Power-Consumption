import streamlit as st
import pandas as pd
import joblib  

model_path = 'E:\\data science\\projact\\Household Power Consumption\\linear_regression_model.pkl'
model = joblib.load(model_path)  
st.title("Household Power Consumption Prediction")
st.write("This app predicts the power consumption based on user data.")

user_data = {
    'Global_reactive_power': st.number_input('Global Reactive Power', min_value=0.0, max_value=10.0, value=0.5),
    'Voltage': st.number_input('Voltage', min_value=210.0, max_value=250.0, value=240.0),
    'Global_intensity': st.number_input('Global Intensity', min_value=0.0, max_value=40.0, value=15.0),
    'Sub_metering_1': st.number_input('Sub Metering 1', min_value=0, max_value=10, value=1),
    'Sub_metering_2': st.number_input('Sub Metering 2', min_value=0, max_value=10, value=1),
    'Sub_metering_3': st.number_input('Sub Metering 3', min_value=0, max_value=10, value=1)
    }


df = pd.DataFrame([user_data])


if st.button('Predict'):
    try:

        prediction = model.predict(df)
        st.success(f"Predicted power consumption: {prediction[0]:.2f} kilowatt-hours.")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
