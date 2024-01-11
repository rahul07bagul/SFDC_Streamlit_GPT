import pandas as pd
import streamlit as st
import time
from datetime import datetime

def showSpinner(timeSec):
    with st.spinner('Loading..'):
        time.sleep(timeSec)

def isFirstPage():
    if st.session_state.on_second_page:
        return False
    return True

def isFourthPage():
    return st.session_state.on_fourth_page

def isFifthPage():
    return st.session_state.on_fifth_page

# Sesstion state varaible intialization
def init():
    if 'on_second_page' not in st.session_state:
        st.session_state.on_second_page = False
    if 'on_fourth_page' not in st.session_state:
        st.session_state.on_fourth_page = False
    if 'on_fifth_page' not in st.session_state:
        st.session_state.on_fifth_page = False

# Load data from CSV file
@st.cache_data   # Cache the loaded data for better performance
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

def is_date_in_current_month(date_str):
    # Parse the input date string into a datetime object
    check_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f%z')

    # Get the current date
    current_date = datetime.now(check_date.tzinfo)

    # Check if the year and month of the provided date match the current year and month
    return check_date.year == current_date.year and check_date.month == current_date.month

def get_total_user_data(users):
    created_in_this_month = 0
    active_user = 0
    for usr in users:
        if is_date_in_current_month(usr["CreatedDate"]):
            created_in_this_month += 1
        if usr["IsActive"]:
            active_user += 1
        
    if created_in_this_month == 0:
        created_in_this_month = None
    return [created_in_this_month, active_user]