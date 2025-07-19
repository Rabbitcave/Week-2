import streamlit as st

def reverse_each_word(sentence: str) -> str:
    # Split sentence into words, reverse each via slicing, then re-join
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

def main():
    st.title("🔄 Reverse Each Word in a Sentence")
    sentence = st.text_input("Enter a sentence:", value="Hello world from Streamlit")
    if sentence:
        result = reverse_each_word(sentence)
        st.write("**Original:**", sentence)
        st.write("**Reversed words:**", result)

if __name__ == "__main__":
    main()
