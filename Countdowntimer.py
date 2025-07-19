import streamlit as st
import time

st.set_page_config(page_title="Countdown Timer")

st.title("Countdown from 10 to 0")

# Placeholder for dynamic metric
ph = st.empty()

def countdown(start=10):
    for secs in range(start, -1, -1):
        ph.metric("Time Remaining ⏳", f"{secs:02d} seconds")
        time.sleep(1)
    ph.metric("Time Remaining ⏳", "Done!")

if st.button("Start Countdown"):
    countdown(10)
