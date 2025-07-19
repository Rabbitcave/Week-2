import streamlit as st

def format_name(parts: list[str]) -> dict[str, str]:
    """Return formatted name variants based on parts."""
    formatted = {}
    n = len(parts)
    if n == 2:
        first, last = parts
        formatted["Last, First"] = f"{last}, {first}"
        formatted["First Last"] = f"{first} {last}"
    elif n >= 3:
        first = parts[0]
        last = parts[-1]
        middles = parts[1:-1]
        initials = "".join(f"{m[0]}." for m in middles)
        formatted["Last, First MiddleInitials"] = f"{last}, {first} {initials}"
        formatted["First MiddleInitials Last"] = f"{first} {initials} {last}"
    else:
        formatted["Error"] = "Please enter at least first and last name."
    return formatted

def main():
    st.title("Name Formatter")

    full_name = st.text_input("Enter your full name", placeholder="e.g. John Michael Smith")
    if full_name:
        parts = full_name.strip().split()
        formatted = format_name(parts)

        st.subheader("Formatted Outputs")
        for label, line in formatted.items():
            if label == "Error":
                st.error(line)
            else:
                st.write(f"**{label}:** {line}")

if __name__ == "__main__":
    main()
