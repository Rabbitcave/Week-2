import streamlit as st
import numpy as np

st.set_page_config(page_title="Number Counter", page_icon="🔢", layout="centered")

# Title and description
st.title("🔢 Number Category Counter")
st.markdown("Enter a list of numbers (separated by commas), and we'll count how many are **positive**, **negative**, and **zero**! ✨")

# Input field
input_str = st.text_input("Enter numbers separated by commas (e.g. 1, -2, 0, 4, -5):")

# Process the input
if st.button("Count"):
    try:
        # Convert input to list of numbers
        numbers = [float(num.strip()) for num in input_str.split(',') if num.strip() != '']

        # Count categories
        positives = sum(1 for num in numbers if num > 0)
        negatives = sum(1 for num in numbers if num < 0)
        zeros = sum(1 for num in numbers if num == 0)

        # Display in 3 columns like cards
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(label="🟢 Positive", value=positives)

        with col2:
            st.metric(label="🔴 Negative", value=negatives)

        with col3:
            st.metric(label="⚪ Zero", value=zeros)

        # Optionally show the full list
        st.success("✅ Numbers processed successfully!")

    except ValueError:
        st.error("❌ Invalid input. Please enter only numbers separated by commas.")
