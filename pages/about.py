import streamlit as st

def show():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader("About This App")
    st.markdown("""
        This Car Price Estimator uses machine learning to predict the market value of your vehicle 
        based on its specifications and condition.
        
        ### How It Works
        1. Enter your car's specifications in the form
        2. Get an initial price estimate
        3. Upload a photo of your car for damage assessment
        4. Receive a final price adjusted for any damage
        
        ### Features
        - Accurate price prediction based on historical data
        - Computer vision damage detection
        - User-friendly interface
        
        ### Model Information
        - Price prediction: Gradient Boosting Regressor
        - Damage detection: ResNet18 CNN
    """)
    st.markdown("</div>", unsafe_allow_html=True)