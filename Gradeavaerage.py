import streamlit as st

# 🚀 Generated using an AI-assisted tool (e.g., GPT) — ready to run in Streamlit

def main():
    st.title("Test Score Averager & Pass/Fail Evaluator")

    # You can replace these with st.number_input if you want interactive inputs
    scores = [75, 82, 59, 90, 68]  # Example 5 test scores

    avg_score = sum(scores) / len(scores)

    status = "Pass" if avg_score >= 60 else "Fail"  # threshold logic

    # Display results
    st.write(f"**Scores:** {scores}")
    st.write(f"**Average Score:** {avg_score:.2f}")
    st.write(f"**Result:** 🟢 {status}" if status == "Pass" else f"**Result:** 🔴 {status}")

if __name__ == "__main__":
    main()
