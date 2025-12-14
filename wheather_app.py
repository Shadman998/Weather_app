import streamlit as st
import requests

# 1. Title and Description
st.title("🌤️ Weather Checker")
st.write("Enter a city name below to get the current weather conditions.")

# 2. Input Widget (Replaces input())
city = st.text_input("Enter City Name:", "Dhaka")

# 3. API Details
# Note: In a real job, never hardcode API keys! Use st.secrets (explained below)
API_KEY = "e25033e7ebcf723100aebf163025aaa8" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# 4. The Button (Controls when the code runs)
if st.button("Get Weather"):
    if city:
        try:
            # Construct URL with f-string and metric units (Celsius)
            url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
            
            # Fetch data
            response = requests.get(url)
            
            # Check if the city was found (Status Code 200)
            if response.status_code == 200:
                data = response.json()
                
                # Extracting key information
                main = data['main']
                weather_desc = data['weather'][0]['description']
                temp = main['temp']
                humidity = main['humidity']
                wind_speed = data['wind']['speed']

                # 5. Display Data (Replaces pprint)
                st.success(f"Weather in {city.title()} found!")
                
                # Layout with columns for a pro look
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Temperature", f"{temp}°C")
                with col2:
                    st.metric("Humidity", f"{humidity}%")
                with col3:
                    st.metric("Wind Speed", f"{wind_speed} m/s")
                
                st.info(f"Condition: {weather_desc.title()}")
                
                # Optional: Show raw JSON if needed
                with st.expander("See Raw Data"):
                    st.json(data)
            
            else:
                st.error("City not found! Please check the spelling.")
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a city name first.")
