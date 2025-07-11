import streamlit as st

st.title("Number Comparator")

# Input fields for two numbers
num1 = st.number_input("Enter the first number:", format="%.2f")
num2 = st.number_input("Enter the second number:", format="%.2f")

# Button to compare
if st.button("Compare"):
    if num1 > num2:
        st.success(f"{num1} is greater than {num2}")
    elif num1 < num2:
        st.warning(f"{num1} is less than {num2}")
    else:
        st.info(f"{num1} is equal to {num2}")