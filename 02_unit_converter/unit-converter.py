import streamlit as st  # Streamlit is a Library for building web apps

# Function to convert units based on predefined conversion factors or formulas
def convert_units(value, unit_from, unit_to):
    
    conversions = {
        'meters_kilometers': 0.001,   # 1 meter = 0.001 kilometer
        'kilometers_meters': 1000,    # 1 kilometer = 1000 meter
        'grams_kilograms': 0.001,     # 1 gram = 0.001 kilogram
        'kilograms_grams': 1000       # 1 kilogram = 1000 gram
    }

    key = f'{unit_from}_{unit_to}'  # Generate a key based on the input and output units

    # Logic to convert units
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return 'Conversion not supported'   # Return a message if the conversion is not supported

st.title('Unit Converter')  # Set the title of the web app

# User input: numerical value to convert
value = st.number_input('Enter the value:')

# Dropdown to select unit to convert from
unit_from = st.selectbox('Convert from:', ['meters', 'kilometers', 'grams', 'kilograms'])

# Dropdown to select unit to convert to
unit_to = st.selectbox('Convert to:', ['meters', 'kilometers', 'grams', 'kilograms'])

# Button to trigger the conversion
if st.button('Convert'):
    result = convert_units(value, unit_from, unit_to)   # Call the conversion function 
    st.write(f'Converted value: {result}')  # Display the result