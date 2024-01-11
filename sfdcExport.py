import streamlit as st
from simple_salesforce import Salesforce
import pandas as pd
import altair as alt

@st.cache_data
def convert_to_csv(data):
    df = pd.DataFrame(data)
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

# Advancecd option section
def show_advanced_options(data):
    st.session_state.advanced_option = True
    data = pd.DataFrame(data)
    
    # Chart conversion options
    chart_type = st.selectbox('Select Chart Type:', ['None','Line Chart', 'Bar Chart', 'Scatter Plot'])
    x_axis = st.selectbox('Select X Axis:', data.columns)
    y_axis = st.selectbox('Select Y Axis:', data.columns)
    group_by_field = st.selectbox('Select Field for Grouping (Optional):', [None] + list(data.columns))

    # Convert table data to the selected chart type
    if chart_type == 'Line Chart':
        st.write('Line Chart:')
        chart = alt.Chart(data).mark_line().encode(
            x=x_axis,
            y=y_axis,
            color=group_by_field if group_by_field else alt.value('steelblue')
        ).properties(
            width=500
        )
        st.altair_chart(chart, use_container_width=True)

    elif chart_type == 'Bar Chart':
        st.write('Bar Chart:')
        chart = alt.Chart(data).mark_bar().encode(
            x=x_axis,
            y=y_axis,
            color=group_by_field if group_by_field else alt.value('steelblue')
        ).properties(
            width=500
        )
        st.altair_chart(chart, use_container_width=True)

    elif chart_type == 'Scatter Plot':
        st.write('Scatter Plot:')
        chart = alt.Chart(data).mark_circle().encode(
            x=x_axis,
            y=y_axis,
            color=group_by_field if group_by_field else alt.value('steelblue')
        ).properties(
            width=500
        )
        st.altair_chart(chart, use_container_width=True)

# Download Button (For CSV)
def download_data(data):
    if data:
        csv = convert_to_csv(data)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='export.csv',
            mime='text/csv'
        )
    else:
        st.warning("No data to donwload")

# Table to show query result
def show_table(result):
    st.write("Query Result:")
    st.table(result)

# Extract the result of query to show in table
def extract_data(result):
    columns = list(result[0].keys())
    columns.remove("attributes")
    # Extracting all data for display
    data_to_display = [{column: record[column] for column in columns} for record in result]
    return data_to_display

# Export button to run query
def export(sf_instance,query):
    # Button to execute export
    if st.button("Export", type="primary"):
        try:
            # Execute the Salesforce query
            result = sf_instance.query_all(query)['records']
            data_to_display = extract_data(result)
            st.session_state.result = data_to_display
            
            if result:
                return data_to_display
            else:
                st.warning("No records found for the given query.")
        except Exception as e:
            st.error(f"Error executing query: {str(e)}")
    elif st.session_state.advanced_option:
        return st.session_state.result

def inspector(_sf_instance):
    # Input for query
    query = st.text_area("Export Query", key="textarea",value="Select id,name from account")
    st.session_state.query = query
    data_to_display = export(_sf_instance,query)
    if data_to_display:
        download_data(data_to_display)
        with st.expander("Show Advanced Export",st.session_state.advanced_option):
            show_advanced_options(data_to_display)
        show_table(data_to_display)

# Sesstion state varaible intialization
def init():
    if 'advanced_option' not in st.session_state:
        st.session_state.advanced_option = False
    if 'result' not in st.session_state:
        st.session_state.result = ""
    if 'query' not in st.session_state:
        st.session_state.query = ""

def export_data(instance):
    init()
    inspector(instance)
