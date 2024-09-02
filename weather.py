import streamlit as st
import pyowm

# Initialize OpenWeatherMap API
API_KEY = 'YOUR_API_KEY'  # Replace with your own API key
owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()

# Title of the application
st.title("Weather Forecast")

# Input field for the city name
city = st.text_input("Enter the city name:")

# Button to get weather
if st.button("Get Weather"):
    if city:
        try:
            # Fetch the weather
            observation = mgr.weather_at_place(city)
            weather = observation.weather
            temperature = weather.temperature('celsius')['temp']
            status = weather.detailed_status
            
            # Display the weather information
            st.success(f"Weather in {city.capitalize()}:")
            st.write(f"Temperature: {temperature:.1f} °C")
            st.write(f"Condition: {status.capitalize()}")
        except:
            st.error("City not found or an error occurred. Please check the city name.")
    else:
        st.error("Please enter a city name.")

# Footer
st.write("Powered by Streamlit & OpenWeatherMap")
