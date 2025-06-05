import pandas as pd

def preprocess_input(name, year, km_driven, fuel, seller_type, 
                    transmission, owner, mileage, engine, max_power, seats):
    """Preprocess user input for prediction"""
    input_df = pd.DataFrame([[name, year, km_driven, fuel, seller_type, 
                            transmission, owner, mileage, engine, max_power, seats]],
        columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 
                'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats'])
    
    # Encoding
    input_df['owner'].replace(['First Owner', 'Second Owner', 'Third Owner',
       'Fourth & Above Owner', 'Test Drive Car'], [1,2,3,4,5], inplace=True)
    input_df['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'], [1,2,3,4], inplace=True)
    input_df['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'], [1,2,3], inplace=True)
    input_df['transmission'].replace(['Manual', 'Automatic'], [1,2], inplace=True)
    input_df['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
       'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
       'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
       'Ambassador', 'Ashok', 'Isuzu', 'Opel'], list(range(1, 32)), inplace=True)
    
    return input_df

def get_brand_name(car_name):
    """Extract brand name from full car name"""
    return car_name.split(' ')[0].strip()