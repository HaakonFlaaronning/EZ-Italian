import streamlit as st
import pandas as pd
import os
import nltk
from nltk.tokenize import sent_tokenize

from utils.data_utils import find_sentence_for_words

nltk.download('punkt')
nltk.download('punkt_tab')

st.set_page_config(
  page_title = 'EZ Italian',
  page_icon = '✅',
  layout = 'wide'
)

st.write("# EZ Italian 😃")

# Load data
common_words_df = pd.read_csv('data/common_words.csv', sep=';')
# Load all stories
num_stories = len(os.listdir('./stories'))
stories = [None] * num_stories
for file in os.listdir('./stories'):
  story_num = int(file.split('_')[0])
  with open(f'stories/{file}', encoding='utf-8') as f:
    stories[story_num] = sent_tokenize(f.read())

common_words_df = find_sentence_for_words(common_words_df, stories)
common_words_df_to_display = common_words_df[['Word', 'Translation', 'Sentence']]
common_words_df_to_display.index += 1

possessive_pronouns_df = pd.read_csv('data/possessive_pronouns.csv', sep=',', index_col=False)
prepositions_df = pd.read_csv('data/prepositions.csv', sep=',', index_col=False)
prepositions_article_df = pd.read_csv('data/preposition_articles.csv', sep=',', index_col=False)


# Inject CSS to force text wrapping in table cells
st.markdown(
  """
  <style>
  table, th, td {
    white-space: pre-wrap;
  }
  </style>
  """,
  unsafe_allow_html=True
)

# Display data using st.dataframe in 5 columns
with st.expander("# De 1000 mest brukte ordene"):
  col1, col2, col3, col4, col5 = st.columns(5)
  n = len(common_words_df_to_display)
  sep1, sep2, sep3, sep4 = n // 5, 2 * n // 5, 3 * n // 5, 4 * n // 5
  with col1:
    st.dataframe(common_words_df_to_display.iloc[:sep1], use_container_width=True, height=35 * sep1 + 38)
  with col2:
    st.dataframe(common_words_df_to_display.iloc[sep1:sep2], use_container_width=True, height=35 * (sep2 - sep1) + 38)
  with col3:
    st.dataframe(common_words_df_to_display.iloc[sep2:sep3], use_container_width=True, height=35 * (sep3 - sep2) + 38)
  with col4:
    st.dataframe(common_words_df_to_display.iloc[sep3:sep4], use_container_width=True, height=35 * (sep4 - sep3) + 38)
  with col5:
    st.dataframe(common_words_df_to_display.iloc[sep4:], use_container_width=True, height=35 * (n - sep4) + 38)

with st.expander("# Possessive pronomen, Preposisjoner"):
  st.write("## Possessive pronomen")
  st.dataframe(possessive_pronouns_df, use_container_width=True, height=35*possessive_pronouns_df.shape[0]+38, hide_index=True)
  
  st.write("## Preposisjoner")
  col1, col2 = st.columns(2)
  with col1: 
    st.dataframe(prepositions_df, use_container_width=True, height=35*prepositions_df.shape[0]+38, hide_index=True) 
  with col2:
    st.dataframe(prepositions_article_df, use_container_width=True, height=35*prepositions_article_df.shape[0]+38, hide_index=True)