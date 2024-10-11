import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = '100 Mest brukte verb',
    layout ='wide'
)
st.write("Verb")

verbs_df = pd.read_csv('data/100verbs.csv', sep=',')
verbs_df.index += 1
st.dataframe(verbs_df)