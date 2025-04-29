import streamlit as st

# -------------------- Password Strength Checker --------------------
def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    special_characters = "!@#$%^&*()-_+=<>?/{}[]|"
    has_special = any(char in special_characters for char in password)

    if length < 6:
        return "Very Weak"
    elif length >= 6 and has_lower and has_digit:
        if has_upper and has_special:
            return "Strong"
        elif has_upper or has_special:
            return "Moderate"
        else:
            return "Weak"
    elif length >= 8:
        return "Weak"
    else:
        return "Very Weak"

# -------------------- Custom CSS Styling --------------------
st.markdown("""
    <style>
    body {
        margin: 0;
        padding: 0;
    }

    .main-title {
        font-size: 48px;
        text-align: center;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 0 0 10px #ff6b81, 0 0 20px #f39c12;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin-bottom: 20px;
    }

    .app-background {
        background: linear-gradient(120deg, #1f1c2c, #928dab);
        height: 100vh;
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        z-index: -1;
    }

    .glass-box {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px;
        width: 500px;
        margin: 50px auto;
        backdrop-filter: blur(15px);
        box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
        color: white;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.18);
    }

    .strength-box {
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
        margin-top: 15px;
        color: white;
    }

    .made-by {
        text-align: center;
        color: #ddd;
        font-size: 14px;
        margin-top: 50px;
    }
    </style>
    <div class='app-background'></div>
""", unsafe_allow_html=True)

# -------------------- UI --------------------
st.markdown("<h1 class='main-title'>🔐 Adeel Khan's VIP Password Checker</h1>", unsafe_allow_html=True)

st.markdown("<div class='glass-box'>", unsafe_allow_html=True)

password = st.text_input("💬 Enter your password:", type="password", key="password_input")

if password:
    strength = check_password_strength(password)

    if strength == "Very Weak":
        st.markdown(f"<div class='strength-box' style='background-color:#e74c3c;'>❌ Very Weak Password</div>", unsafe_allow_html=True)
        st.warning("Use uppercase, lowercase, numbers & special characters.")
    elif strength == "Weak":
        st.markdown(f"<div class='strength-box' style='background-color:#f39c12;'>⚠️ Weak Password</div>", unsafe_allow_html=True)
        st.info("Add uppercase letters and symbols for better strength.")
    elif strength == "Moderate":
        st.markdown(f"<div class='strength-box' style='background-color:#3498db;'>ℹ️ Moderate Password</div>", unsafe_allow_html=True)
        st.info("Almost there! Add special characters to make it stronger.")
    elif strength == "Strong":
        st.markdown(f"<div class='strength-box' style='background-color:#2ecc71;'>✅ Strong Password</div>", unsafe_allow_html=True)
        st.success("Great job! Your password is secure.")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------- Footer --------------------
st.markdown("<div class='made-by'>Made with ❤️ by Adeel Khan using Python + Streamlit</div>", unsafe_allow_html=True)
