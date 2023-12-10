import streamlit as st

import expander

st.title("URL Expander")
st.write("This app expands shortened URLs to their original form.")
shortened_url = st.text_input("Enter a shortened URL")
button = st.button("Expand URL")
if button:
    expanded_url = expander.expand_link(shortened_url)
    # write the expanded URL to the app as a clickable link
    st.markdown(f"Expanded URL: [{expanded_url}]({expanded_url})")
