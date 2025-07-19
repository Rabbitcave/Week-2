import streamlit as st

def count_vowels(word: str) -> int:
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in word if ch in vowels)

def main():
    st.title("Vowel Counter 🎯")

    word = st.text_input("Enter a word:", value="Hello")
    if word:
        count = count_vowels(word)
        st.write(f"Word: **{word}**")
        st.success(f"Number of vowels: **{count}**")

if __name__ == "__main__":
    main()
