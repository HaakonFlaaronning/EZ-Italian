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

# Load data
common_words_df = pd.read_csv('data/common_words.csv', sep=';')
common_words_df.index += 1
indirect_pronouns_df = pd.read_csv('data/indirect_pronouns.csv', sep='|')
indirect_pronouns_df.index +=1

# Display data
with st.expander("# De 1000 mest brukte ordene"):
  col1, col2, col3, col4, col5 = st.columns(5)
  sep1, sep2, sep3, sep4 = len(common_words_df)//5, 2*len(common_words_df)//5, 3*len(common_words_df)//5, 4*len(common_words_df)//5
  with col1:
    st.dataframe(common_words_df.iloc[:sep1], use_container_width=True, height=35*sep1+38)
  with col2:
    st.dataframe(common_words_df.iloc[sep1:sep2], use_container_width=True, height=35*sep1+38)
  with col3:
    st.dataframe(common_words_df.iloc[sep2:sep3], use_container_width=True, height=35*sep1+38)
  with col4:
    st.dataframe(common_words_df.iloc[sep3:sep4], use_container_width=True, height=35*sep1+38)
  with col5:
    st.dataframe(common_words_df.iloc[sep4:], use_container_width=True, height=35*sep1+38)
st.dataframe(indirect_pronouns_df)
