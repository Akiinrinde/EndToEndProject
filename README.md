# EndToEndProject
# Superstore Profit Prediction

An application for predicting profit based on sales data using a Machine Learning model, FastAPI, and Streamlit.

## Table of Contents

- [Description](#description)
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Project Flow](#project-flow)
- [Role of FastAPI](#role-of-fastapi)
  

## Description

The Superstore Profit Prediction project is an end-to-end data science project that involves the analysis of sales data and the development of a machine learning model to predict profit. The project also includes the creation of a Streamlit web application that allows users to input sales-related data and receive profit predictions. FastAPI is used to create the API that handles the communication between the Streamlit app and the machine learning model.

## Project Overview

The project can be summarized in the following steps:

1. **Data Analysis**: The project starts with data analysis using Python and Pandas. The data is read from a CSV file ("cleaned_superstore.csv"), and various aspects of the data are explored, including data cleansing and preprocessing.

2. **Machine Learning Model**: A machine learning model, possibly a Linear Regression model, is developed to predict profit based on sales-related features. The model is trained and evaluated to ensure its predictive accuracy.

3. **FastAPI API**: FastAPI is used to create an API that serves as the interface between the Streamlit web application and the machine learning model. The API accepts input data, sends it to the model, and returns the prediction.

4. **Streamlit App**: A Streamlit web application is created to provide a user-friendly interface for profit prediction. Users can select a category, sub-category, sales, quantity, and discount, and the app will send this data to the FastAPI API.

5. **Integration**: The Streamlit app is integrated with the FastAPI API, allowing seamless communication between the user interface and the model.

6. **Prediction and Display**: The model predicts profit, and the result is displayed back to the user in the Streamlit app.

7. **Deployment**: The application, including the FastAPI API and Streamlit app, is deployed to a server or platform where it can be accessed by users.

## Role of FastAPI

FastAPI plays a crucial role in the project:

- **API Development**: FastAPI is used to develop a fast and efficient API that handles incoming requests from the Streamlit app. It defines the endpoints and the data schema, ensuring that requests are properly validated.

- **Data Validation**: FastAPI automatically validates the data received from the Streamlit app, ensuring that it matches the expected format and data types.

- **Model Integration**: FastAPI integrates with the machine learning model, passing the input data to the model for prediction and returning the results to the Streamlit app.

- **Real-time Interaction**: FastAPI enables real-time interaction between the user interface (Streamlit) and the model, allowing users to receive predictions quickly.

- **Scalability**: FastAPI is designed for high performance and scalability, making it suitable for serving multiple users simultaneously.

## Getting Started

### Prerequisites

- Python 3.x
- Pandas 
- Scikit-learn 
- Streamlit 
- FastAPI


