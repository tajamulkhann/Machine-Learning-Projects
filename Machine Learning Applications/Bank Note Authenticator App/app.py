# -*- coding: utf-8 -*-

import numpy as np
import pickle
import streamlit as st
from PIL import Image

# Load the trained model
with open("classifier.pkl", "rb") as file:
    classifier = pickle.load(file)

# Prediction function
def predict_note_authentication(variance, skewness, curtosis, entropy):
    input_data = [[variance, skewness, curtosis, entropy]]
    prediction = classifier.predict(input_data)
    return prediction[0]

# Streamlit App
def main():
    st.set_page_config(page_title="Bank Note Authenticator", page_icon="💸", layout="centered")

    # Sidebar
    with st.sidebar:
        st.image("https://avatars.githubusercontent.com/u/107360623?v=4", caption="Tajamul Khan", width=120)
        st.markdown("## 🔍 About")
        st.markdown("""
        **App Name:** Bank Note Authenticator  
        **Author:** Tajamul Khan  
        **Model:** Trained on UCI Bank Note Dataset  
        **Connect:** [LinkedIn](https://www.linkedin.com/in/tajamulkhann/)
        """)

    # Header
    st.markdown("<h1 style='text-align: center; color: #ff6347;'>💰 Bank Note Authenticator</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Predict whether a bank note is real or fake using ML!</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Input form with columns
    col1, col2 = st.columns(2)

    with col1:
        variance = st.text_input("📉 Variance", placeholder="e.g. 2.3")

    with col2:
        skewness = st.text_input("📊 Skewness", placeholder="e.g. 4.1")

    col3, col4 = st.columns(2)

    with col3:
        curtosis = st.text_input("📈 Curtosis", placeholder="e.g. 1.5")

    with col4:
        entropy = st.text_input("🌪️ Entropy", placeholder="e.g. -1.2")

    st.markdown("")

    result = ""

    if st.button("🔍 Predict"):
        try:
            # Convert inputs to float
            variance = float(variance)
            skewness = float(skewness)
            curtosis = float(curtosis)
            entropy = float(entropy)

            # Prediction
            prediction = predict_note_authentication(variance, skewness, curtosis, entropy)
            result = "✅ The note is **Authentic**." if prediction == 1 else "❌ The note is **Fake**."
            st.success(result)

        except ValueError:
            st.error("🚫 Please enter valid numeric values in all fields.")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; font-size: 12px;'>
        © 2025 <b>Tajamul Khan</b> | Built with ❤️ using Streamlit <br>
        <a href='https://www.linkedin.com/in/tajamulkhann/' target='_blank'>🔗 Connect on LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()
