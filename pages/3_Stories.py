import streamlit as st
import pandas as pd
import os

st.set_page_config(
  page_title='Historier',
  page_icon='🐲',
  layout='wide'
)

# -- Checkbox to toggle translation visibility (global for all stories) --
if 'show_translation' not in st.session_state:
  st.session_state.show_translation = False

def toggle_translation():
  st.session_state.show_translation = not st.session_state.show_translation

st.write("# Historier 🐲")

# -- Gather all .txt story files from stories folder --
stories_dir = "stories"
story_files = [f for f in os.listdir(stories_dir) if f.endswith(".txt")]
# Sort files by the leading numeric part in the filename
story_files = sorted(story_files, key=lambda x: int(x.split('_')[0]))

# -- Loop over each story file --
for story_file in story_files:
  # Extract the base name without extension
  base_name = story_file[:-4]  # e.g. "0_three_little_piggies"
  parts = base_name.split('_')  # ["0", "three", "little", "piggies"]
  
  # The first element is the numeric index, the rest form the title
  story_index = parts[0]
  story_title = " ".join(parts[1:]).title()  # "Three Little Piggies"
  
  # Read the story text, then split on ';;;' for the two versions
  with open(os.path.join(stories_dir, story_file), encoding='utf-8') as f:
    story_content = f.read()
  it_text, no_text = story_content.split(';;;')
  
  # -- Display each story inside an expander --
  with st.expander(f"# {story_title}"):
    # Button to show/hide translation
    st.button("Vis/Gjem oversettelse", on_click=toggle_translation, key=story_file)
    
    col1, col2 = st.columns(2)
    with col1:
      st.write("## (IT) " + story_title)
      st.write(it_text.strip())
    with col2:
      if st.session_state.show_translation:
        st.write("## (ENG) " + story_title)
        st.write(no_text.strip())
