import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import plotly.graph_objects as go
from sfdcConnect import *
from sfdcBot import chat
from streamlit_echarts import st_echarts
from sfdcRest import *
from sfdcExport import *
from utils import *

sf_instance = None #SF Instance

# Connect to Salesforce
@st.cache_data
def connect():
    return connect_sfdc()

# Main function to create the Streamlit app
def main():
    st.set_page_config(layout="wide",page_title="SFDC Analytics")
    init()

    # Salesforce Connection
    global sf_instance 
    sf_instance = connect()

    # Page title
    st.title("SFDC Analytics")
    sidebar_menu()

# Side Bar Menu
def sidebar_menu():
    page1 = st.sidebar.button("Analysis")
    page2 = st.sidebar.button("Object Limits")
    page3 = st.sidebar.button("Territory Modal")
    page4 = st.sidebar.button("Chat Bot")
    page5 = st.sidebar.button("Data Export")

    st.markdown(
        """
        <style>
            div.stButton > button {
                border: none !important;
                width: 100%;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    if page1:
        st.session_state.on_second_page = False
        st.session_state.on_fourth_page = False
        st.session_state.on_fifth_page = False
        render_page1()
    elif page2:
        showSpinner(3)
        render_page2()
    elif page3:
        showSpinner(3)
        render_page3()
    elif page4:
        showSpinner(3)
        render_page4()
    elif page5:
        showSpinner(3)
        render_page5()
    else:
        if isFifthPage() and not isFourthPage():
            render_page5()
        elif isFourthPage():
            render_page4()
        elif isFirstPage():
            render_page1()
        else:
            render_page2()

def home_page():
    st.title("SFDC Analytics")

# Menu Option 1 Screen
def render_page1():
    showSpinner(5)
    total_counts()

    col1, col2 = st.columns(2)

    with col1:
        pie_chart()
    with col2:
        line_chart()

    col3, col4 = st.columns(2)
    with col3:
        bubble_chart()
    with col4:
        monthly_users()

    important_sets()
    venn_diagram()

# Menu Option 2 Screen
def render_page2():
    gauge_chart_limits()

# Menu Option 3 Screen
def render_page3():
    territory_tree()

# Menu Option 4 Screen
def render_page4():
    st.session_state.on_fourth_page = True
    chat()

# Menu Option 5 Screen
def render_page5():
    st.session_state.on_fifth_page = True
    global sf_instance
    export_data(sf_instance)

# Execute salesforce query
def execute_query(query):
    try:
        return sf_instance.query_all(query)['records']
    except Exception as e:
        st.error(f"Error executing query: {str(e)}")

# Total Counts
@st.cache_data
def total_counts():
    container = st.container(border=True)
    total_objects = execute_query(constants.QUERY_OBJECTS)
    total_permission_sets = execute_query(constants.QUERY_TOTAL_PERMISSION_SETS)
    total_profiles = execute_query(constants.QUERY_TOTAL_PROFILES)
    total_packages = execute_query(constants.QUERY_TOTAL_PACKAGES)
    
    users = execute_query(constants.QUERY_USERS)
    total_users = len(users)
    active_delta, total_active = get_total_user_data(users)

    col1, col2, col3 = container.columns(3)
    col1.metric(label="Total Objects", value=len(total_objects))
    col2.metric(label="Total Profiles", value=total_profiles[0]['expr0'])
    col3.metric(label="Total Packages", value=total_packages[0]['expr0'])

    col4, col5, col6 = container.columns(3)
    col4.metric(label="Total Users", value=total_users,delta=active_delta)
    col5.metric(label="Total Active Users", value=total_active)
    col6.metric(label="Total Permission Sets", value=total_permission_sets[0]['expr0'])

# Pie Chart - Permission Set Usage
@st.cache_data
def pie_chart():
    container = st.container(border=True)
    query = constants.QUERY_PERMISSION_SET_ASSIGNMENT
    
    result = execute_query(query)
    
    if result:
        data = [
            dict(id=rec['Id'], PermissionSetName=rec['PermissionSet']['Name'])
            for rec in result
            if not rec['PermissionSet']['Name'].startswith("X00")
        ]
        data = pd.DataFrame(data)

        # Get the count of each unique value in 'PermissionSet.Name'
        count_data = data['PermissionSetName'].value_counts().reset_index()
        count_data.columns = ['PermissionSetName', 'Count']

        # Create a pie chart using Plotly Express
        fig = px.pie(count_data, names='PermissionSetName', values='Count')

        # Display the pie chart
        container.subheader("Permission Set Usage")
        container.plotly_chart(fig)
    else:
        container.warning("No records found for the given query.")

# Line Chart - Permission Set Assignment
@st.cache_data
def line_chart():
    container = st.container(border=True)
    query = constants.QUERY_PERMISSION_SET_ASSIGNMENT
    result = execute_query(query)

    if result:
        data = [
            dict(id=rec['Id'], PermissionSetName=rec['PermissionSet']['Name'], SystemModstamp=rec['SystemModstamp'])
            for rec in result
            if not rec['PermissionSet']['Name'].startswith("X00")
        ]
        data = pd.DataFrame(data)

        # Extract month names from SystemModstamp
        data['MonthName'] = pd.to_datetime(data['SystemModstamp']).dt.month_name()

        # Group data by month name and permission set, and count assignments
        count_data = data.groupby(['MonthName', 'PermissionSetName'])['id'].count().unstack()

        fig = px.line(count_data, x=count_data.index, y=count_data.columns)

        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Number of Assignments",
            width=800, 
            height=450, 
            margin=dict(l=50, r=50, t=50, b=50)
        )
        container.subheader("PermissionSet Assignment Count by Month")
        container.plotly_chart(fig)
    else:
        container.warning("No records found for the given query.")       

# Bubble Chart - Account Revenue by Country
@st.cache_data
def bubble_chart():
    container = st.container(border=True)
    query = constants.QUERY_ACCOUNTS
    result = execute_query(query)

    if result:
        data = [dict(Id=rec['Id'], BillingCountry=rec['BillingCountry'],AnnualRevenue=rec['AnnualRevenue'])
               for rec in result]
        data = pd.DataFrame(data)
        
        # Group by 'Country' and calculate the count of accounts and total revenue
        country_summary = data.groupby('BillingCountry').agg({'Id': 'count', 'AnnualRevenue': 'sum'}).reset_index()
        country_summary.columns = ['BillingCountry', 'Count', 'Revenue']

        # Create a bubble chart using Plotly Express
        fig = px.scatter(country_summary, x='Revenue', y='Count', size='Count', color='BillingCountry',
                         labels={'Count': 'Number of Accounts', 'Revenue': 'Revenue'},
                         size_max=60)
        container.subheader("Account Distribution by Country")
        container.plotly_chart(fig)
    else:
        container.warning("No records found for the given query.") 

# Bar Chart - Monthly Users
@st.cache_data
def monthly_users():
    container = st.container(border=True)
    query = constants.QUERY_USERS
    result = execute_query(query)

    if result:
        data = pd.DataFrame(result)

        # Convert CreatedDate to datetime and extract month
        data['Month'] = pd.to_datetime(data['CreatedDate']).dt.month_name()
        user_counts_by_month = data.groupby('Month')['Id'].count()

        fig = px.bar(
            user_counts_by_month,
            x=user_counts_by_month.index, 
            y='Id',
            labels={'Id': 'Number of Users'}
        )
        container.subheader("Monthly New Users")
        container.plotly_chart(fig)
    else:
        container.warning("No records found for the given query.") 

# Table to show which important permissions are enabled
@st.cache_data
def important_sets():
    container = st.container(border=True)

    query = constants.QUERY_PERMISSION_SETS
    result = execute_query(query)

    if result:
        fields_to_extract = set()
        for rec in result:
            fields_to_extract.update(rec.keys())

        # Creating a dictionary with fields as keys and values as lists
        data_dict = {field: [rec.get(field) for rec in result] for field in fields_to_extract}

        data = pd.DataFrame(data_dict)

        # List of permissions to check
        permissions_to_check = [
            "PermissionsViewAllData",
            "PermissionsViewAllProfiles",
            "PermissionsModifyAllData",
            "PermissionsModifyMetadata",
            "PermissionsViewSecurityCommandCenter",
            "PermissionsManageInternalUsers",
            "PermissionsAssignPermissionSets",
            "PermissionsManageProfilesPermissionsets",
            "PermissionsAuthorApex"
        ]

        # Filter data based on permissions
        filtered_data = data[data[permissions_to_check].any(axis=1)]
        columns_to_display = filtered_data[['Name'] + permissions_to_check]        
        columns_to_display.reset_index(drop=True, inplace=True)
        # Display the table
        container.subheader("Permission Sets with critical permissions are enabled")
        container.write(columns_to_display)
    else:
        container.warning("No records found for the given query.") 

# Venn Diagram - Permission Set Overlap
def venn_diagram():
    container = st.container(border=True)
    
    query = constants.QUERY_PERMISSION_SETS
    result = execute_query(query)

    if result:
        fields_to_extract = set()
        for rec in result:
            fields_to_extract.update(rec.keys())

        # Creating a dictionary with fields as keys and values as lists
        data_dict = {field: [rec.get(field) for rec in result] for field in fields_to_extract}

        data = pd.DataFrame(data_dict)
        st.set_option('deprecation.showPyplotGlobalUse', False)

        container.subheader("Permission Set Overlap")

        # Select two permission sets for the Venn diagram
        permission_set_names = container.multiselect("Select two PermissionSet Names", data["Name"].unique())
        if len(permission_set_names) == 2:
            # Filter data for the selected permission sets
            set1_data = data[data["Name"] == permission_set_names[0]]
            set2_data = data[data["Name"] == permission_set_names[1]]
            # Create sets for the Venn diagram
            set1 = set(set1_data.columns[set1_data.iloc[0] == True])
            set2 = set(set2_data.columns[set2_data.iloc[0] == True])
            # Calculate the intersection and unique elements
            intersection = set1.intersection(set2)
            unique_set1 = set1 - set2
            unique_set2 = set2 - set1
            # Display the Venn diagram
            container.subheader("Venn Diagram")
            plt.figure(figsize=(3, 3))
            venn2([len(unique_set1), len(unique_set2), len(intersection)],
                  set_labels=(permission_set_names[0], permission_set_names[1]))
            container.pyplot()
    else:
        container.warning("No records found for the given query.") 

@st.cache_data
# Get object data for all objects
def get_object_data():
    object_result = execute_query(constants.QUERY_OBJECTS)
    object_options = ["None"]
    for obj in object_result:
        object_options.append(obj["QualifiedApiName"])
    return object_options

# Gauge Charts : Limits of each objects
def gauge_chart_limits():
    st.session_state.on_second_page = True
    query_limits = "SELECT EntityDefinitionId,DurableId, Max, Remaining from EntityLimit WHERE EntityDefinition.DeveloperName = "
 
    container = st.container(border=True)
    object_options = get_object_data()

    object = container.selectbox("Select a Object", object_options)

    if object == 'None':
        return

    query = query_limits + "'"+object+"'"

    showSpinner(3)

    object_data = tooling_query(query)
    if object_data:
        data = pd.DataFrame(object_data['records'])
        durable_ids = data['DurableId'].unique()
        columns_per_row = 2
        # Iterate through durable IDs and arrange them in rows and columns
        for i in range(0, len(durable_ids), columns_per_row):
            row_data = durable_ids[i:i + columns_per_row]

            # Create columns for each Durable ID in the row
            cols = container.columns(columns_per_row)

            for j, durable_id in enumerate(row_data):
                subset_data = data[data['DurableId'] == durable_id]
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=int(subset_data['Max']) - int(subset_data['Remaining']),
                    domain={'x': [0, 1], 'y': [0, 1]},
                    title={'text': durable_id,'font': {'size': 24}},
                    gauge={'axis': {'range': [0, int(subset_data['Max'])]}},
                    number={'font': {'size': 40, 'family': 'Arial'}}
                ))

                fig.update_layout(height=350)
                # Display the chart container in the respective column
                cols[j].plotly_chart(fig, use_container_width=True, height=250)

def convert_to_tree(df):
    root_nodes = df[df['Type'] == 'Root']

    tree_data = {"name": "FY26", "children": []}

    for _, root_row in root_nodes.iterrows():
        root_node = {"name": root_row['Name'], "children": [], "collapsed": False}
        tree_data["children"].append(root_node)

        branch_nodes = df[df['Parent'] == root_row['Name']]

        for _, branch_row in branch_nodes.iterrows():
            branch_node = {"name": branch_row['Name'], "children": [], "collapsed": False}
            root_node["children"].append(branch_node)

            leaf_nodes = df[df['Parent'] == branch_row['Name']]

            for _, leaf_row in leaf_nodes.iterrows():
                leaf_node = {"name": leaf_row['Name'], "value": leaf_row['Type']}
                branch_node["children"].append(leaf_node)

    return tree_data

# Tree structure of territories
def territory_tree():

    file = 'data\SFDC Data - Territory.csv'

    if file is not None:
        # Load data from CSV
        data = load_data(file)

        # Generate tree
        tree_data = convert_to_tree(data)

        opts = {
            "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
            "series": [
                {
                    "type": "tree",
                    "data": [tree_data],
                    "top": "1%",
                    "left": "7%",
                    "bottom": "1%",
                    "right": "20%",
                    "symbolSize": 7,
                    "label": {
                        "position": "left",
                        "verticalAlign": "middle",
                        "align": "right",
                        "fontSize": 9,
                    },
                    "leaves": {
                        "label": {
                            "position": "right",
                            "verticalAlign": "middle",
                            "align": "left",
                        }
                    },
                    "expandAndCollapse": True,
                    "animationDuration": 550,
                    "animationDurationUpdate": 750,
                }
            ],
        }   

        # Display the ECharts chart using Streamlit
        st_echarts(opts, height=2500, theme="dark")

if __name__ == "__main__":
    main()
