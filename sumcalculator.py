import streamlit as st
import time

st.set_page_config(page_title="Sum from 1 to N", page_icon="➕", layout="centered")

st.title("➕ Sum of Numbers from 1 to N")
st.markdown("Let's **add all numbers** from `1` to any number `n` you choose — the classic math problem made interactive! 🎯")

# User input for N
n = st.number_input("Enter a positive integer (n):", min_value=1, step=1)

# Button to calculate
if st.button("Calculate Sum"):
    st.info("🔄 Calculating the sum using a loop...")

    total = 0
    steps = ""

    progress = st.progress(0)
    status = st.empty()

    # Loop to calculate the sum
    for i in range(1, int(n) + 1):
        total += i
        steps += f"{i} "
        status.text(f"Adding: {steps.strip()} = {total}")
        progress.progress(i / n)
        time.sleep(0.05)  # for animation effect

    st.success(f"✅ The sum of numbers from 1 to {int(n)} is **{total}** 🎉")

    st.markdown(f"""
        ---
        ### 🧠 Did You Know?
        You can also use the formula:  
        \n**Sum = n × (n + 1) / 2**  
        For `n = {int(n)}`, that's `{int(n)} × ({int(n)} + 1) / 2 = {int(n * (n + 1) // 2)}`
    """)

