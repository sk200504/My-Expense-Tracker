import streamlit as st
import pandas as pd
import os

FILE = "expenses.csv"

# Create file if not exists
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE, index=False)

st.title("💰 Student Expense Tracker")

# Input fields
date = st.date_input("Select Date")
category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Other"])
amount = st.number_input("Amount", min_value=0)

if st.button("Add Expense"):
    new_data = pd.DataFrame([[date, category, amount]],
                            columns=["Date", "Category", "Amount"])
    new_data.to_csv(FILE, mode='a', header=False, index=False)
    st.success("Expense Added!")

# Load data
df = pd.read_csv(FILE)

st.subheader("📊 Expense Data")
st.write(df)

# Total
st.subheader("💵 Total Expense")
st.write(df["Amount"].sum())

# Chart
st.subheader("📈 Category-wise Spending")
chart = df.groupby("Category")["Amount"].sum()
st.bar_chart(chart)