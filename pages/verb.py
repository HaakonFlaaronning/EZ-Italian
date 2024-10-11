import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = '100 Mest brukte verb',
    layout ='wide'
)
st.write("Verb")

colnames = ['Verb', 'Oversettelse', 'Link']
verbs_df = pd.read_csv('data/verbs.csv', sep=',', names =colnames, header=None)
verbs_df.index += 1

st.data_editor(
    verbs_df,
    column_config={
        'Link': st.column_config.LinkColumn(
            'Bøyning', display_text='clicky'
        ),
    },
    hide_index=True,
)
#st.dataframe(verbs_df.style.format({'Links': lambda x: f'<a href="{x}">Link</a>'}), escape_html=False)

#Sidebar
st.sidebar.page_link('1_Casa.py', label='Casa')
st.sidebar.page_link('pages/verb.py', label='100 mest brukte verb')
st.sidebar.page_link('pages/2_Sah_Dude.py', label='Suhdude')