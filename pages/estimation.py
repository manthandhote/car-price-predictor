import os
import streamlit as st
import pandas as pd
import torch
from PIL import Image
from utils.models import load_regression_model, load_damage_model
from utils.preprocessing import preprocess_input, get_brand_name
from utils.config import CLASS_NAMES, TRANSFORM

def predict_damage(image, model):
    """Predict if car is damaged"""
    image_tensor = TRANSFORM(image.copy()).unsqueeze(0)
    with torch.no_grad():
        output = model(image_tensor)
        _, predicted = torch.max(output, 1)
    return CLASS_NAMES[predicted.item()]

def estimate_price(base_price, status):
    """Adjust price based on damage status"""
    return base_price * 0.7 if status == 'Damage' else base_price

def show():
    # Load models
    model = load_regression_model()
    damage_model = load_damage_model()
    
    # Load and preprocess data - UPDATED PATH
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'Cardetails.csv')
    cars_data = pd.read_csv(data_path)
    cars_data['name'] = cars_data['name'].apply(get_brand_name)


    with st.container():
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        
        st.subheader("🚘 Car Specifications")
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.selectbox('Car Brand', cars_data['name'].unique(), key='brand')
            year = st.slider('Manufactured Year', 1994, 2024, 2015, key='year')
            km_driven = st.slider('Kilometers Driven', 11, 200000, 50000, key='km_driven')
            fuel = st.selectbox('Fuel Type', cars_data['fuel'].unique(), key='fuel')
            seller_type = st.selectbox('Seller Type', cars_data['seller_type'].unique(), key='seller_type')
            
        with col2:
            transmission = st.selectbox('Transmission', cars_data['transmission'].unique(), key='transmission')
            owner = st.selectbox('Owner', cars_data['owner'].unique(), key='owner')
            mileage = st.slider('Mileage (km/l)', 10, 40, 20, key='mileage')
            engine = st.slider('Engine (CC)', 700, 5000, 1500, key='engine')
            max_power = st.slider('Max Power (bhp)', 0, 200, 100, key='max_power')
            seats = st.slider('Number of Seats', 2, 10, 5, key='seats')
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Predict base price
    if st.button("📊 Calculate Base Price", key='predict'):
        input_df = preprocess_input(name, year, km_driven, fuel, seller_type,
                                   transmission, owner, mileage, engine, max_power, seats)
        base_price = model.predict(input_df)[0]
        st.session_state.base_price = round(base_price, 2)
        st.balloons()
    
    # Display base price if available
    if 'base_price' in st.session_state:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.subheader("💰 Price Estimation Results")
        
        st.markdown(f"""
            <div class='price-display'>
                Predicted Base Price: ₹ {st.session_state.base_price:,}
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.subheader("🔍 Damage Assessment")
        
        uploaded_file = st.file_uploader("Upload a clear photo of your car", 
                                       type=["jpg", "jpeg", "png"], key='uploader')
        
        if uploaded_file is not None:
            col1, col2 = st.columns(2)
            with col1:
                image = Image.open(uploaded_file).convert("RGB").copy()
                st.image(image, caption="Uploaded Car Image", use_container_width=True)
            
            if st.button("🔎 Assess Damage & Final Price", key='assess'):
                with st.spinner('Analyzing car image...'):
                    status = predict_damage(image, damage_model)
                    final_price = estimate_price(st.session_state.base_price, status)
                    
                    with col2:
                        st.markdown(f"""
                            <div class='damage-status {'damage' if status == 'Damage' else 'whole'}'>
                                Car Condition: <strong>{status}</strong>
                            </div>
                            <div class='price-display'>
                                Final Estimated Price: ₹ {round(final_price, 2):,}
                            </div>
                        """, unsafe_allow_html=True)
                        
                        if status == 'Damage':
                            st.warning("The car has visible damage. Price has been adjusted accordingly.")
                        else:
                            st.success("The car appears to be in good condition with no visible damage.")
        
        st.markdown("</div>", unsafe_allow_html=True)   