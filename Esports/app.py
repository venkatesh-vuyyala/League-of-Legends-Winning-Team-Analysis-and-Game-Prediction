import streamlit as st
import numpy as np
import base64


def XGB_model(input_data):
    return np.random.choice(["Win", "Lose"])

# Function to set background image
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded_string = base64.b64encode(data).decode()
    
    page_bg_img = f"""
    <style>
    .stApp {{
    background-image: url("data:image/png;base64,{encoded_string}");
    background-size: cover;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Streamlit app
st.title("League of Legends Game Prediction")

# Set background image
image_file = "lol-02.png"  # Ensure this file is in the same directory
set_background(image_file)

st.header("Enter Game Details")

# Input fields for game details (customize as per your model requirements)
team_1 = st.text_input("Team 1")
team_2 = st.text_input("Team 2")
average_kills = st.number_input("Average Kills", min_value=0)
average_deaths = st.number_input("Average Deaths", min_value=0)
average_assists = st.number_input("Average Assists", min_value=0)

if st.button("Predict"):
    input_data = {
        "team_1": team_1,
        "team_2": team_2,
        "average_kills": average_kills,
        "average_deaths": average_deaths,
        "average_assists": average_assists
    }
    result = XGB_model(input_data)
    st.write(f"The prediction is: {result}")
