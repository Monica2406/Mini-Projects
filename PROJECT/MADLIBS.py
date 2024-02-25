#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def mad_libs():
   
    story_template = "Once upon a time, there was a {noun1} who loved to {verb1}. One day, they met a {adjective1} {noun2} who wanted to {verb2} with them. Together, they {adverb1} {verb3} into the {noun3} and found a {adjective2} {noun4}. The end."
    parts_of_speech = {
        'noun1': input("Enter a noun: "),
        'verb1': input("Enter a verb: "),
        'adjective1': input("Enter an adjective: "),
        'noun2': input("Enter a noun: "),
        'verb2': input("Enter a verb: "),
        'adverb1': input("Enter an adverb: "),
        'verb3': input("Enter a verb: "),
        'noun3': input("Enter a noun: "),
        'adjective2': input("Enter an adjective: "),
        'noun4': input("Enter a noun: ")
    }
    story = story_template.format(**parts_of_speech)
    print("\nHere's your Mad Libs story:\n")
    print(story)


mad_libs()


# In[ ]:




