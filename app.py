import streamlit as st
import re

# Set up the page
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

# Title and description
st.title("🔐 Password Strength Checker")
st.markdown(""" 
### Welcome to the ultimate password strength checker!
Make your passwords stronger! Our tool quickly evaluates how secure your password is.
""")

# Toggle to show/hide password
show_password = st.checkbox("Show Password")
password = st.text_input("Enter your password", type="default" if show_password else "password", help="Ensure your password is strong")

# Common weak passwords list
common_passwords = ["123456", "password", "12345678", "qwerty", "abc123"]

# Initialize
feedback = []
score = 0
max_score = 5

# Password strength logic
if password:
    # Common password check
    if password.lower() in common_passwords:
        feedback.append("❌ This is a commonly used password. Choose something more unique.")
    else:
        score += 1

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Case sensitivity check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Use both UPPER and lower case letters.")

    # Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    # Special character check
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Level Display
    st.markdown("### Password Strength:")
    st.progress(score / max_score)

    if score == 5:
        st.success("✅ Strong Password 💪")
    elif score >= 3:
        st.warning("🟡 Medium Strength – Can be improved")
    else:
        st.error("🔴 Weak Password – Needs improvement!")

    # Show feedback
    if feedback:
        st.markdown("### Suggestions to Improve:")
        for item in feedback:
            st.write(item)
else:
    st.info("Please enter your password to get started.")
