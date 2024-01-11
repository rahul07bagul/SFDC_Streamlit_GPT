# Salesforce + Streamlit + GPT

## Introduction 

I've created a basic data science project using **Salesforce** as the data source. To make it user-friendly, I've leveraged **Streamlit**, a powerful tool for data science projects. The project revolves around permission analysis, focusing on features not readily available in Salesforce. The dashboards I've built showcase permission set usage, and their significance, and highlight which permissions are enabled. One handy feature is the ability to export data using Salesforce queries and visualize it through various charts based on user preferences. Additionally, I've integrated **OpenAI's** GPT to facilitate easy interaction. You can ask the chatbot questions, helping you quickly find permissions and profiles. While most features use real-time data, GPT uses CSV files to train on Salesforce permission set assignment and object permission data. This combination makes it a comprehensive tool for diving into Salesforce permissions effortlessly.

## Features
- Permission Set Usage (Pie Chart)
- Total Counts (Profiles/Permission Sets/Packages/Users)
- Permission Set Assignment Analysis (Line Chart)
- Account Revenue By Country (Bubble Chart)
- Monthly New Users (Bar Chart)
- Review for which permission sets important permission is enabled (Table)
- Permission Set Overlap (Venn Diagram)
- Object Limits (Gauge Chart)
- Tree structure of Territory Modal
- Chat Bot (OpenAI - gpt-3.5-turbo)
- Data Export

## Configuration

Use your credentials (constants.py):
```python
APIKEY = "<OpenAI Key>"

# Salesforce credentials
USERNAME = '<your_username>'
PASSWORD = '<your_password>'
SECURITY_TOKEN = '<security_token>' #you will find this in user settings
DOMAIN = '.my.salesforce.com'
DOMAIN_FULL = "https://<your_domain>.my.salesforce.com"
CONSUMER_KEY = "<consumer_key>" #create connected app in salesforce and then use consumer key here
CONSUMER_SECRET = "<consumer_secret>" #create connected app in salesforce and then use consumer key here
```

## Preview

- Total Counts (Profiles/Permission Sets/Packages/Users)
<img width=1200 src="https://github.com/rahul07bagul/SFDC_Streamlit_GPT/blob/main/screenshots/Counts.png" alt="bench">

| Permission Set Usage (Pie Chart)     | Permission Set Assignment Analysis (Line Chart)              |
| ----------: | :------------------- |
| <img width=1200 src="https://github.com/rahul07bagul/SFDC_Streamlit_GPT/blob/main/screenshots/PieChart.png" alt="bench">  | <img width=1200 src="https://github.com/rahul07bagul/SFDC_Streamlit_GPT/blob/main/screenshots/LineChart.png" alt="bench"> |

| Account Revenue By Country (Bubble Chart)     | Monthly New Users (Bar Chart)             |
| ----------: | :------------------- |
| <img width=1200 src="https://github.com/rahul07bagul/SFDC_Streamlit_GPT/blob/main/screenshots/BubbleChart.png" alt="bench">  | <img width=1200 src="https://github.com/rahul07bagul/SFDC_Streamlit_GPT/blob/main/screenshots/BarChart.png" alt="bench"> |

- Review for which permission sets important permission is enabled (Table)
<img width=1200 src="https://github.com/rahul07bagul/SFDC_Streamlit_GPT/blob/main/screenshots/ImportantSets.png" alt="bench">

- Permission Set Overlap (Venn Diagram)
<img width=1200 src="https://github.com/rahul07bagul/SFDC_Streamlit_GPT/blob/main/screenshots/VennDiagram.png" alt="bench">

- Object Limits (Gauge Chart)
<img width=1200 src="https://github.com/rahul07bagul/SFDC_Streamlit_GPT/blob/main/screenshots/GaugeChart.png" alt="bench">

- Tree structure of Territory Modal
<img width=1200 src="https://github.com/rahul07bagul/SFDC_Streamlit_GPT/blob/main/screenshots/Tree.png" alt="bench">

---

- Chat Bot (Using OpenAI)
<img width=1200 src="https://github.com/rahul07bagul/SFDC_Streamlit_GPT/blob/main/screenshots/Bot1.png" alt="bench">
<img width=1200 src="https://github.com/rahul07bagul/SFDC_Streamlit_GPT/blob/main/screenshots/Bot2.png" alt="bench">

---

- Data Export
<img width=1200 src="https://github.com/rahul07bagul/SFDC_Streamlit_GPT/blob/main/screenshots/Export1.png" alt="bench">
<img width=1200 src="https://github.com/rahul07bagul/SFDC_Streamlit_GPT/blob/main/screenshots/Export2.png" alt="bench">
