import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = '100 Mest brukte verb',
    page_icon='📚',
    layout ='wide'
)
st.write("# Verb 📚")

# Load data
verbs_df = pd.read_csv('data/verbs.csv', sep=',')
verbs_df.index += 1

irr_verbs_df = pd.read_csv('data/irregular_verbs.csv', sep=';')
irr_verbs_df.index += 1
reflexive_verbs_df = pd.read_csv('data/reflexive_verbs.csv', sep=';')
reflexive_verbs_df.index += 1

# The most common 100 verbs
with st.expander("# De mest brukte 100 verbene"):
  col1, col2, col3 = st.columns(3)
  first_third, second_third = verbs_df.shape[0] // 3, 2 * verbs_df.shape[0] // 3
  with col1:
    st.dataframe(verbs_df.iloc[:first_third], use_container_width=True, height=35*first_third+38)
  with col2:
    st.dataframe(verbs_df.iloc[first_third:second_third], use_container_width=True, height=35*first_third+38)
  with col3:
    st.dataframe(verbs_df.iloc[second_third:], use_container_width=True, height=35*first_third+38)

# Irregular verbs
with st.expander("# Uregelmessige verb"):
  col1, col2 = st.columns(2)
  half_len = irr_verbs_df.shape[0] // 2
  with col1:
    st.dataframe(irr_verbs_df.iloc[:half_len], use_container_width=True, height=35*half_len+38)
  with col2:
    st.dataframe(irr_verbs_df.iloc[half_len:], use_container_width=True, height=35*half_len+38)

# Reflexive verbs
with st.expander("Refleksive verb"):
  st.dataframe(reflexive_verbs_df, use_container_width=True, height=35*len(reflexive_verbs_df)+38)