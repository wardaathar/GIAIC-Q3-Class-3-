import streamlit as st # type: ignore #try 
import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    if len(password) >= 8:
        strength += 1
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'\d', password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1

    if strength == 4:
        remarks = "💪 Strong Password"
    elif strength == 3:
        remarks = "🙂 Good Password"
    elif strength == 2:
        remarks = "😕 Weak Password"
    else:
        remarks = "😞 Very Weak Password"

    return remarks

# Streamlit UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    result = check_password_strength(password)
    st.subheader("Result:")
    st.success(result)
