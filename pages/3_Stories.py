import streamlit as st
import pandas as pd

st.set_page_config(
  page_title = 'Historier',
  page_icon = '✅',
  layout = 'wide'
)

# Checkbox to toggle translation visibility
if 'show_translation' not in st.session_state:
    st.session_state.show_translation = False

def toggle_translation():
    st.session_state.show_translation = not st.session_state.show_translation

# Load stories
with open('stories/three_little_piggies.txt', encoding='utf-8') as f:
  three_little_piggies = f.read()
it_three_little_piggies, no_three_little_piggies = three_little_piggies.split(';;;')

st.write("# Historier")

# De 3 små grisene
with st.expander("# De 3 små grisene"):
  # Button to show/hide translation
  st.button("Vis/Gjem oversettelse", on_click=toggle_translation)
  
  col1, col2 = st.columns(2)
  with col1:
    st.write("## I tre porcellini")
    st.write(it_three_little_piggies)
  with col2:
    if st.session_state.show_translation:
      st.write("## De tre små grisene")
      st.write(no_three_little_piggies)