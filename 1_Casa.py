import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

st.set_page_config(
  page_title = 'EZ Italian',
  page_icon = '✅',
  layout = 'wide'
)

st.write("# EZ Italian 😃")

sen = sent_tokenize("test. ok.")
st.write(sen)

# Load data
common_words_df = pd.read_csv('data/common_words.csv', sep=';')
common_words_df.index += 1

possessive_pronouns_df = pd.read_csv('data/possessive_pronouns.csv', sep=',', index_col=False)

prepositions_df = pd.read_csv('data/prepositions.csv', sep=',', index_col=False)

prepositions_article_df = pd.read_csv('data/preposition_articles.csv', sep=',', index_col=False)

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

with st.expander("# Possessive pronomen, Preposisjoner"):
  st.write("## Possessive pronomen")
  st.dataframe(possessive_pronouns_df, use_container_width=True, height=35*possessive_pronouns_df.shape[0]+38, hide_index=True)
  
  st.write("## Preposisjoner")
  col1, col2 = st.columns(2)
  with col1: 
    st.dataframe(prepositions_df, use_container_width=True, height=35*prepositions_df.shape[0]+38, hide_index=True) 
  with col2:
    st.dataframe(prepositions_article_df, use_container_width=True, height=35*prepositions_article_df.shape[0]+38, hide_index=True)