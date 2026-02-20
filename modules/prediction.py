import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from database.db_connection import get_connection

mydb = get_connection()

st.header("Expense Prediction")

df = pd.read_sql("SELECT * FROM expenses", mydb)

if not df.empty:

    df["date"] = pd.to_datetime(df["date"])
    df["day"] = df["date"].dt.day

    X = df[["day"]]
    y = df["amount"]

    model = LinearRegression()
    model.fit(X, y)

    future_day = st.number_input("Enter future day of month", min_value=1, max_value=31)

    if st.button("Predict"):
        prediction = model.predict([[future_day]])
        st.success(f"Predicted Expense: {prediction[0]:.2f}")

else:
    st.write("Not enough data for prediction.")
