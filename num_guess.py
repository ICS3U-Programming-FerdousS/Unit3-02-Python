#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: March 23, 2022
# This program asks the user for a number 1-9
# then if check if they guessed it right or wrong
# and tell them the right number


import constants


def main():
    # ask user for a number between 1-9
    guess_number = int(input("Enter a number between 1-9 "))
    print("")

    # check if the guessed the right number 
    if guess_number == constants.THE_NUMBER:
        print("You guessed it right!")
    else:
    # display the right number if they guessed it wrong
        print("You guessed it wrong")
        print("The right number was ", constants.THE_NUMBER)


if __name__ == "__main__":
    main()
