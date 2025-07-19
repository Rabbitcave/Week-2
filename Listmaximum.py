import streamlit as st

# 🚀 AI-generated code: Finds max manually without built‑ins

def find_largest(numbers):
    if not numbers:
        return None
    # Initialize with the first element
    largest = numbers[0]
    # Compare each value
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

def main():
    st.title("Find Largest Number (without max())")

    # You can change this list or make it interactive
    numbers = [23, 5, 87, 42, 67]

    st.write("Numbers:", numbers)

    largest = find_largest(numbers)
    if largest is not None:
        st.success(f"The largest number is **{largest}**")
    else:
        st.error("No numbers provided!")

if __name__ == "__main__":
    main()
