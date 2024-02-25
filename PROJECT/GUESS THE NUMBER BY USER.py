#!/usr/bin/env python
# coding: utf-8

# In[1]:


def guess_the_number():
    print("Welcome to Guess the Number!")
    print("Think of a number between 1 and 100.")
    print("I will try to guess it.")
    
    low = 1
    high = 100
    attempts = 0
    
    while True:
        guess = (low + high) // 2
        print(f"My guess is: {guess}")
        attempts += 1
        
        feedback = input("Is my guess too high (H), too low (L), or correct (C)? ").upper()
        
        if feedback == "C":
            print(f"I guessed the number in {attempts} attempts!")
            break
        elif feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1
        else:
            print("Invalid input. Please enter H, L, or C.")

guess_the_number()


# In[ ]:




