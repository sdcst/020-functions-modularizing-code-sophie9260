"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""

def title():
    print("Guessing game!")
    print("Here are the instructions on how to play: please guess a number from 1 to 5, keep guessing until you get it right.")

def game():
    n = ""
    while n != 4:
        n =  input("Guess a number from 1 to 5 => ")
        n = float(n)
        if n != 4:
            print("Wrong guess... try again!")
            print("===     ===")
        else:
            print("Good job you guessed it!")

title()
game()