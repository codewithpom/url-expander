import concurrent.futures

import pandas as pd
import requests
import streamlit as st


def expand_link(short_url):
    try:
        response = requests.head(short_url, allow_redirects=True)
        return response.url
    except requests.RequestException as e:
        return f"Error during request: {e}"

def expand_bulk_links(short_urls):
    expanded_urls = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Use map to apply the function to each URL concurrently
        expanded_urls = list(executor.map(expand_link, short_urls))
    return expanded_urls

# Example usage
# shortened_urls = ["http://bit.ly/47P80uh", 'https://t.co/CU6kPyRA5z', "https://t.co/1g10UnHmhr"]
'''
http://bit.ly/47P80uh
https://t.co/CU6kPyRA5z
https://t.co/1g10UnHmhr
'''
def main():
    st.title("Bulk Expander")
    st.write("Add all your shortened URLs in the text area below and click on the button to expand them.")
    # Add content for the bulk expander page here
    shortened_urls = st.text_area("Enter shortened URLs", value="", height=200)
    if st.button("Expand URLs"):
        data = {"Shortened URL": [], "Expanded URL": []}
        short_urls = shortened_urls.split("\n")
        s = short_urls
        expanded_urls = expand_bulk_links(short_urls)
        for short_url, expanded_url in zip(s, expanded_urls):
            data["Shortened URL"].append(short_url)
            data["Expanded URL"].append(expanded_url)
        df = pd.DataFrame(data)
        # show the dataframe with caption and without index
        st.table(df.style.set_caption("Expanded URLs").hide(axis="index"))
        # download the dataframe as csv file
        st.download_button(
            label="Download CSV",
            data=df.to_csv().encode("utf-8"),
            file_name="expanded_urls.csv",
            mime="text/csv",
        )


            
