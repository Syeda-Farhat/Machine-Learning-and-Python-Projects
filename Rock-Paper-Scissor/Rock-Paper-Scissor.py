#!/usr/bin/env python
# coding: utf-8

# # Rock-Paper-Scissor Game Project in Python

# ### Importing Required Libraries

# In[1]:


import random       #generates random values
import os          #use system specific paremeters and functions
import re           #use Regular Expression


# In[4]:


while (1<2): # creating a continuous loop
    
    # Define Game
    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")

    # input from user
    user_input = input("Choose your option [R]ock], [P]aper, [S]cissors, [E]xit: ")
    
    # Validating the user input
    if (not re.match("[SsRrPpEe]", user_input)) or (len(user_input) != 1):
        print ("Please selecton your option:")
        print ("[R]ock, [S]cissors, [P]aper or [E]xit")
        continue

    # Print the user's choice
    print ("You chose: " + user_input)

    # Check if user wants to exit
    if (user_input == 'E' or user_input == 'e' ):
        print('Exiting Game..')
        break

    # Create a list of possible choices
    selection = ['R', 'P', 'S']
    
    # Generating Computer's Choice
    opponenetChoice = random.choice(selection)
    
    # Print Computer's Choice
    print ("I chose: " + opponenetChoice)

    # Check Computer's Choice and user's Choice by applying game logic
    
    if opponenetChoice == str.upper(user_input):         # If both chose same value, it's a tie
        print ("Tie! ")
    
    elif opponenetChoice == 'R' and user_input.upper() == 'S':            # Rock Vs Scissor - Rock/computer Wins
        print ("Scissors beats rock, I win! ")
        continue
    elif opponenetChoice == 'S' and user_input.upper() == 'P':            # Scissor Vs Paper - Paper/computer Wins
        print ("Scissors beats paper! I win! ")
        continue
    elif opponenetChoice == 'P' and user_input.upper() == 'R':            # Paper Vs Rock - Paper/computer Wins
        print ("Paper beat rock, I win! ")
        continue
    else:                                                                 # In all the other cases, user wins!
        print ("You win!")

