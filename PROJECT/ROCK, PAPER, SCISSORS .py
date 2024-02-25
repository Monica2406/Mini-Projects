#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: Rock, Paper, or Scissors.")
    
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    while True:
        user_choice = input("Your choice: ").lower()
        
        if user_choice not in choices:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")
            continue
        
        print(f"Computer's choice: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or              (user_choice == 'paper' and computer_choice == 'rock') or              (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

play_game()


# In[ ]:




