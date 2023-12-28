from supabase import create_client
import pandas as pd 
import streamlit as st 
import plotly.express as px

API_URL = 'https://ujgwymeolqkoryelbzwv.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVqZ3d5bWVvbHFrb3J5ZWxiend2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODEzMTU5ODAsImV4cCI6MTk5Njg5MTk4MH0.W3brkkJfG1MgfNxNqm12KDS71mBCrJMAs7E0Dm_lX7o'
supabase = create_client(API_URL, API_KEY)

supabaseList = supabase.table('maintable').select('*').execute().data

df = pd.DataFrame()
for row in supabaseList:
    row["created_at"] = row["created_at"].split(".")[0]
    row["time"] = row["created_at"].split("T")[1]
    row["date"] = row["created_at"].split("T")[0]
    row["DateTime"] = row["created_at"]
    df = df.append(row, ignore_index=True)


st.set_page_config(page_title="Dashboard",layout='centered', initial_sidebar_state='collapsed')

st.markdown('### Temperature')
fig = px.line(df, x="DateTime", y="temperature", title='',markers=True)
st.plotly_chart(fig,use_container_width=True)

st.markdown('### Humidity')
fig = px.line(df, x="DateTime", y="humidity", title='',markers=True)
st.plotly_chart(fig,use_container_width=True)

st.markdown('### Moisture')
fig = px.line(df, x="DateTime", y="moisture", title='',markers=True)
st.plotly_chart(fig,use_container_width=True)