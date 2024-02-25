#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

def choose_word():
    words = ["python", "hangman", "computer", "programming", "code", "algorithm", "developer", "software", "debugging"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def get_guess(guessed_letters):
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha() or guess in guessed_letters:
        print("Invalid guess. Please enter a single letter you haven't guessed before.")
        return get_guess(guessed_letters)
    else:
        return guess

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
            if attempts == 0:
                print("Sorry, you've run out of attempts. The word was:", word)
                break
        
        displayed = display_word(word, guessed_letters)
        print(displayed)
        
        if "_" not in displayed:
            print("Congratulations! You've guessed the word:", word)
            break

hangman()


# In[ ]:




