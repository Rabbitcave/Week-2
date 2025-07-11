import streamlit as st

st.title("Password Validator")

# Minimum password length requirement
MIN_LENGTH = 8

# Input password (using password input for privacy)
password = st.text_input("Enter your password:", type="password")

if st.button("Validate Password"):
    if len(password) >= MIN_LENGTH:
        st.success("✅ Password is valid.")
    else:
        st.error(f"❌ Password too short. Must be at least {MIN_LENGTH} characters long.")
