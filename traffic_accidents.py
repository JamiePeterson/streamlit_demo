import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Set page config to have a wide layout
st.set_page_config(layout="wide")

# Load data
url = os.path.join(os.path.dirname(__file__), 'ardd_fatalities.csv')
data = pd.read_csv(url)

# Preprocess data
df = data.copy()
df['Month'] = df['Month'].apply(lambda x: f"{x:02d}")
df['date_str'] = df['Month'].astype(str) + '-' + df['Year'].astype(str)
df['date_obj'] = pd.to_datetime(df['date_str'], format='%m-%Y')

# Top Insights
state_counts = df['State'].value_counts().reset_index()
state_counts.columns = ['State', 'Number of Crashes']

month_counts = df['Month'].value_counts().reset_index()
month_counts.columns = ['Month', 'Number of Crashes']

day_counts = df['Dayweek'].value_counts().reset_index()
day_counts.columns = ['Day of Week', 'Number of Crashes']

time_counts = df['Time'].value_counts().reset_index()
time_counts.columns = ['Time of Day', 'Number of Crashes']

crash_type_counts = df['Crash Type'].value_counts().reset_index()
crash_type_counts.columns = ['Crash Type', 'Number of Crashes']

age_group_counts = df['Age Group'].value_counts().reset_index()
age_group_counts.columns = ['Age Group', 'Number of Crashes']

christmas_counts = df[df['Christmas Period'] == 'Yes'].shape[0]
easter_counts = df[df['Easter Period'] == 'Yes'].shape[0]

regional_counts = df['National Remoteness Areas'].value_counts().reset_index()
regional_counts.columns = ['Region', 'Number of Crashes']

road_user_counts = df['Road User'].value_counts().reset_index()
road_user_counts.columns = ['Road User', 'Number of Crashes']

# Streamlit app with white background and color theme
st.markdown("""
<style>
    body {
        background-color: white;
    }
    .header {
        background-color: #e03a3e;
        color: white;
        padding: 20px;
        text-align: center;
    }
    .footer {
        background-color: #FFA500;
        color: white;
        padding: 10px;
        text-align: center;
        font-size: 12px;
        position: fixed;
        bottom: 0;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown('<div class="header">Australian Traffic Accident Analysis</div>', unsafe_allow_html=True)

# Sidebar for insights
st.sidebar.header('Insights')
insight = st.sidebar.radio(
    "Select an insight to view:",
    ("State-wise Distribution", "Monthly Trends", "Day of the Week", "Time of Day", "Crash Type", "Age Group", "Holiday Period", "Regional Trends", "Road User Trends")
)

if insight == "State-wise Distribution":
    st.markdown('### State-wise Distribution of Crashes')
    st.markdown("This visualization shows the number of traffic accidents by state. It helps identify which states have higher accident rates.")
    fig = px.bar(state_counts, x='State', y='Number of Crashes', color='State', title='Number of Crashes by State')
    st.plotly_chart(fig)

elif insight == "Monthly Trends":
    st.markdown('### Monthly Trends in Crashes')
    st.markdown("This visualization shows the monthly trends in traffic accidents. It helps to identify which months have higher accident rates.")
    fig = px.bar(month_counts, x='Month', y='Number of Crashes', color='Month', title='Number of Crashes by Month')
    st.plotly_chart(fig)

elif insight == "Day of the Week":
    st.markdown('### Day of the Week Analysis')
    st.markdown("This visualization shows the number of traffic accidents by day of the week. It helps to understand which days have more accidents.")
    fig = px.bar(day_counts, x='Day of Week', y='Number of Crashes', color='Day of Week', title='Number of Crashes by Day of the Week')
    st.plotly_chart(fig)

elif insight == "Time of Day":
    st.markdown('### Time of Day Analysis')
    st.markdown("This visualization shows the number of traffic accidents by time of day. It helps to highlight when accidents are most frequent.")
    fig = px.bar(time_counts, x='Time of Day', y='Number of Crashes', color='Time of Day', title='Number of Crashes by Time of Day')
    st.plotly_chart(fig)

elif insight == "Crash Type":
    st.markdown('### Crash Type Analysis')
    st.markdown("This visualization shows the number of traffic accidents by type (single vs. multiple). It helps to understand the nature of crashes.")
    fig = px.bar(crash_type_counts, x='Crash Type', y='Number of Crashes', color='Crash Type', title='Number of Crashes by Type')
    st.plotly_chart(fig)

elif insight == "Age Group":
    st.markdown('### Age Group Involvement')
    st.markdown("This visualization shows the number of traffic accidents by age group. It helps to understand which age groups are most affected.")
    fig = px.bar(age_group_counts, x='Age Group', y='Number of Crashes', color='Age Group', title='Number of Crashes by Age Group')
    st.plotly_chart(fig)

elif insight == "Holiday Period":
    st.markdown('### Holiday Period Analysis')
    st.markdown("This section highlights the number of traffic accidents during the Christmas and Easter periods.")
    st.markdown(f'**Number of Crashes during Christmas Period**: {christmas_counts}')
    st.markdown(f'**Number of Crashes during Easter Period**: {easter_counts}')

elif insight == "Regional Trends":
    st.markdown('### Regional Crash Trends')
    st.markdown("This visualization shows the number of traffic accidents by region. It helps to understand the distribution of accidents in different regions.")
    fig = px.bar(regional_counts, x='Region', y='Number of Crashes', color='Region', title='Number of Crashes by Region')
    st.plotly_chart(fig)

elif insight == "Road User Trends":
    st.markdown('### Trends by Road User')
    st.markdown("This visualization shows the number of traffic accidents by road user type. It helps to understand the involvement of different road users in accidents.")
    fig = px.bar(road_user_counts, x='Road User', y='Number of Crashes', color='Road User', title='Number of Crashes by Road User')
    st.plotly_chart(fig)

# Add footnote with data source information
st.markdown("""
**Data Source**: [Australian Road Deaths Database (ARDD)](https://data.gov.au/dataset/ds-dga-5b530fb8-526e-4fbf-b0f6-aa24e84e4277/details?q=road%20deaths)
*Bureau of Infrastructure and Transport Research Economics*  
*Created 13/07/2015  / Updated 11/12/2023*  
The Australian Road Deaths Database provides basic details of road transport crash fatalities in Australia as reported by the police each month to the State and Territory road safety authorities. Road deaths from recent months are preliminary and the series is subject to revision.
""")

# Add copyright footnote
st.markdown('<div class="footer">© 2024 Jamie Peterson</div>', unsafe_allow_html=True)
