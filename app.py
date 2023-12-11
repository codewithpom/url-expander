import streamlit as st

from normal_expander import main as normal_expander
from bulk_expander import main as bulk_expander

def page_about():
    st.title("About Page")
    st.write("This is the about page.")
    # Add content for the about page here



# Sidebar navigation
page_options = ["Normal Expander", "Bulk Expander"]
selected_page = st.sidebar.selectbox("Choose a page", page_options)

# Display the selected page
if selected_page == "Normal Expander":
    normal_expander()
elif selected_page == "Bulk Expander":
    bulk_expander()
