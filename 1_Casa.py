import streamlit as st
import pandas as pd

pd.set_option('display.max_column', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_seq_items', None)
pd.set_option('display.max_colwidth', 500)
pd.set_option('expand_frame_repr', True)

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
