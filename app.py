import streamlit
import requests
import json
import pandas as pd

df = pd.read_csv("cleaned_superstore.csv")

def run():
    streamlit.title("Profit Prediction")
    category = streamlit.selectbox("Category", df.Category.unique())
    sub_category = streamlit.selectbox("sub_category", df['sub_category'].unique())
    sales = streamlit.number_input("Sales")
    quantity = streamlit.number_input("Quantity")
    discount = streamlit.number_input("Discount")
    
    data = { 
        'Category': category,
        'sub_category': sub_category,
        'Sales': sales,
        'Quantity': quantity,
        'Discount': discount,
        }
    
    if streamlit.button("Predict"):
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        prediction =response.text
        streamlit.success(f"The prediction from model: {prediction}")
        
if __name__ == '__main__':
    #by default it will run at 8501 port
    run()