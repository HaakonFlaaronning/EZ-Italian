import streamlit as st
import pandas as pd

st.set_page_config(
  page_title = 'EZ Italian',
  page_icon = '✅',
  layout = 'wide'
)

st.write("# EZ Italian 😃")

# Load most common words
common_words_df = pd.read_csv('data/common_words.csv', sep=',')
common_words_df.index += 1
st.dataframe(common_words_df)

indirect_pronouns_df = pd.read_csv('data/indirect_pronouns.csv', sep='|')
indirect_pronouns_df.index +=1
st.dataframe(indirect_pronouns_df)


#Sidebar
st.sidebar.page_link('1_Casa.py', label='Casa')
st.sidebar.page_link('pages/verb.py', label='100 mest brukte verb')
st.sidebar.page_link('pages/2_Sah_Dude.py', label='Suhdude')