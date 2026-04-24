## Setup
- `file_o_investigate.py`

## Instructions
Look at the following code and make sure you understand it! Once you do, you are going to make a change!

Right now, the game only keeps track of scores, but I want you to keep track of usernames too! Before the user "plays the game", ask the user to enter in their username. The file output should store both the user's name and score in a format like this:
```plaintext
username: 50
```

## Starter code
```python
"""
author:
date:
Play a game and collect points
"""
import random


def play_game():
    """Play an intense game, and return the score for that round
    
    Returns:
        int: The score for playing this round
    """
    return random.randint(1, 50)

def main():
    # Input
    yes_no = input("Do you want to play a game? ")

    # Processing
    scores = []
    # Check to see if the input (when converted to lowercase) 
    # starts with "y"
    while yes_no.lower().startswith("y"):
        # TODO: ask for username

        # Play the game and print the score
        score = play_game()
        print(f"Woah! Nice round. Your score was {score}")

        # Add the score to the scores list. Notice two things
        ## 1. I need to convert score to a str 
        ##    (f_out.writelines() needs a list of strings)
        ## 2. I need to add on a "\n" (new line character) to the end.
        ##    (Take it out and see what happens)
        # TODO: add the username to follow the format from the instructions
        scores.append(str(score)+"\n")

        # Ask again to ensure we don't have an infinite loop
        yes_no = input("Do you want to play a game? ")
    
    # Output
    # Write all of the scores to a text file scores.txt. 
    # It does not have to exist before we run this program.
    with open("scores.txt", mode="w") as f_out:
        f_out.writelines(scores)


if __name__ == "__main__":
    main()
```