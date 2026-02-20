import streamlit as st

st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", 
                        ["Expense Management", 
                         "Dashboard", 
                         "Prediction"])

if page == "Expense Management":
    import modules.expense_management

elif page == "Dashboard":
    import modules.dashboard

elif page == "Prediction":
    import modules.prediction
