import streamlit as st  # Importing the Streamlit Library for creating the web app
import random   # Importing the random Library for generating random characters
import string   # Imporing the string Library for using string characters



# Function to generate a password based on the user's preferences
def generate_passwod(length, use_digits, use_special):
    characters = string.ascii_letters   # Includes all letters (a-z, A-Z)

    if use_digits:
        characters += string.digits # Adds numbers (0-9) if selected

    if use_special:
        characters += string.punctuation    # Adds special characters (!, @, #, $, %, ^, &, *) if selected

    # Generates a random password of the specified length using the characters defined above
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI setup
st.title('Password Generator')   # Display the app title on the web page


# User input: password length (slider to select length between 6 and 32 characters)
length = st.slider('Select Password Length', min_value = 6, max_value = 32, value = 12)

# Checkbox options for including numbers and special characters in the password
use_digits = st.checkbox('Include Digits')  # Checkbox for numbers (0-9)

use_special = st.checkbox('Include Special Characters') # Checkbox for special characters (!@#$%^&*)

# Button to generate password
if st.button('Generate Password'):
    password = generate_passwod(length, use_digits, use_special)     # Call the password generation function
    
    st.write(f'Generated Password: `{password}`')   # Display the generated password

st.write('---')

st.write('Build with ❤️ by [Tayyaba Hussain](https://github.com/tayyabahussain98)')