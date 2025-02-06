import pandas as pd
import numpy as np

def find_sentence_for_words(words_df, stories):
  # Iterate through words df
  for i, row in words_df.iterrows():
    sentence_references = eval(row['Sentence references']) # List containing entries of [storynum_sentnum, storynum_sentnum, ...]
    if len(sentence_references) == 0:
      continue
    # Select random sentence reference
    random_index = np.random.randint(0, len(sentence_references))
    story_num, sent_num = sentence_references[random_index].split('_')
    # Get sentence from stories
    sentence = stories[int(story_num)][int(sent_num)]
    words_df.at[i, 'Sentence'] = sentence
    print(sentence)
  return words_df
    
    
    