import constants
import streamlit as st
from simple_salesforce import Salesforce

@st.cache_data
def connect_sfdc():
    """Create a Salesforce connection and cache it for performance."""
    return Salesforce(username=constants.USERNAME, password=constants.PASSWORD, security_token=constants.SECURITY_TOKEN)