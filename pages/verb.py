import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = '100 Mest brukte verb',
    layout ='wide'
)
st.write("Verb")

verbs_df = pd.read_csv('data/verbs.csv', sep=',')
verbs_df.index += 1
st.dataframe(verbs_df)


#Sidebar
st.sidebar.page_link('1_Casa.py', label='Casa')
st.sidebar.page_link('pages/verb.py', label='100 mest brukte verb')
st.sidebar.page_link('pages/2_Sah_Dude.py', label='Suhdude')