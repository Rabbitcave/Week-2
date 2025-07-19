import streamlit as st

def main():
    st.title("Name Length Viewer")

    # Store 5 names in a list
    names = ["Alice", "Bob", "Charlotte", "David", "Eleanor"]

    st.write("Here are the names and their lengths:")

    # Display each name and its length
    for name in names:
        st.write(f"- **{name}** has {len(name)} characters")

if __name__ == "__main__":
    main()
