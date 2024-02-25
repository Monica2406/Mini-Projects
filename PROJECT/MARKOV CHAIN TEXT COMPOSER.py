#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def create_markov_chain(corpus, order=1):
    markov_chain = {}
    for i in range(len(corpus) - order):
        prefix = tuple(corpus[i:i+order])
        suffix = corpus[i+order]
        if prefix not in markov_chain:
            markov_chain[prefix] = []
        markov_chain[prefix].append(suffix)
    return markov_chain

def generate_text(markov_chain, length=100):
    current_prefix = random.choice(list(markov_chain.keys()))
    result = list(current_prefix)
    for _ in range(length):
        next_word = random.choice(markov_chain.get(current_prefix, ['']))
        result.append(next_word)
        current_prefix = tuple(result[-len(current_prefix):])
    return ' '.join(result)

# Example usage
corpus = "This is a sample text for demonstrating Markov chain text composition. Markov chains are stochastic models that describe a sequence of possible events in which the probability of each event depends only on the state attained in the previous event. They have various applications, including text generation, speech recognition, and more."
corpus = corpus.split()
order = 2
markov_chain = create_markov_chain(corpus, order)
generated_text = generate_text(markov_chain, length=50)
print(generated_text)


# In[ ]:




