import streamlit as st
import requests

# Title of the application
st.title("Random Quote Generator")

# Button to fetch a random quote
if st.button("Get Random Quote"):
    try:
        # Fetch a random quote from the API
        response = requests.get("https://api.quotable.io/random")
        data = response.json()
        
        # Display the quote and the author
        st.subheader(data['content'])
        st.write(f"— {data['author']}")
    except Exception as e:
        st.error(f"Error fetching quote: {str(e)}")

# Footer
st.write("Powered by Streamlit & Quotable API")
