#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Toby with a simple menu to start up with.
Toby doesnt do anything, just presents a menu with some choices.
You should add functionality to Toby.
"""

def menu():
    """
    Menu
    """
    TOBY_IMAGE = r"""
                               |        |
                               |\      /|
                               | \____/ |
                               |  /\/\  |
                              .'___  ___`.
                             /  \|/  \|/  \
            _.--------------( ____ __ _____)
         .-' \  -. | | | | | \ ----\/---- /
       .'\  | | / \` | | | |  `.  -'`-  .'
      /`  ` ` '/ / \ | | | | \  `------'\
     /-  `-------.' `-----.       -----. `---.
    (  / | | | |  )/ | | | )/ | | | | | ) | | )
     `._________.'_____,,,/\_______,,,,/_,,,,/ 
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(TOBY_IMAGE)
    print("Hi, I'm Toby. I know it all. What can I do you for?")
    print("1) Present yourself to Toby.")
    print("2) Would you like to convert temperature Celsius to Fahrenheit?")
    print("3) Find out your grade on your test.")
    print("4) Calculate numbers and find out the average")
    print("5) Fun concatenation of messages")
    print("6) Number comparison")
    print("7) Check for valid social security numbers.")
    print("8) Check out my skills in the robber language.")
    print("9) Create your own social security number")
    print("10) Create acronym")
    print("11) Make a random word")
    print("12) Find all indexes in a given word")
    print("13) Search for country")
    print("14) Show emission change for a country")

    print("q) Quit.")
    print("") # whitespace
    print("") # whitespace

    print("Try out my 'inv' commands!")
    print("-------------")


def greet():
    """
    Greets user
    """
    name = input("What is your name? ")
    print("\nToby says:\n")
    print(f"Howdy {name}!")
    print("What's up?")

def celcius_to_fahrenheit():
    """
    Converts celcius to fahreneheit
    """
    try:
        tempc = round(float(input("\nPlease enter the temperature in Celsius"
                                    " that you would like to convert to Fahrenheit. Meow: ")),2,)
        tempf = round(tempc * (9 / 5) + 32, 2)
        print(f"{tempc}C is {tempf}F")
    except ValueError:
        print("Toby says:")
        print("Please enter a number in integer instead.")

def points_to_grade():
    """
    Lets the user input their score on a test and get a result back.
    """
    score = int(input("Please enter the score in % "
                        "you got from your test to find out your grade:\n"))

    if score >= 90:
        print("You got an A!")
    elif score >= 80:
        print("You got an B!")
    elif score >= 70:
        print("You got an C!")
    elif score >= 60:
        print("You got an D!")
    elif score < 60:
        print("You got an F!")
    else:
        print("Please enter your score from 1-100%")

def sum_and_average():
    """
    Takes numbers as input and outputs the total and the average of those numbers
    """
    COUNTER = 0
    NEW_TOTAL = 0
    while True:
        number = input("Enter a number or type 'done' ")
        if number == "done":
            break
        else:
            try:
                number = float(number)
            except ValueError:
                print("Please enter a number.")
                continue
            COUNTER += 1
            NEW_TOTAL += number
            average = NEW_TOTAL / COUNTER
    print(f"The sum of all numbers are {NEW_TOTAL}"
            f" and the average of those numbers are {average}")

def hyphen_string():
    """
    Takes a string input and displays the string with added letters and "-"
    """
    NEW_STRING = ""
    COUNTER = 1
    string = input("Toby wants you to enter a message for him: ")
    while len(string) < 1:
        print("Please enter a message")
        string = input("Toby wants you to enter a message for him: ")
    for letter in string:
        for _ in range(COUNTER):
            NEW_STRING += letter
        NEW_STRING += "-"
        COUNTER += 1
    NEW_STRING = NEW_STRING[: len(NEW_STRING) - 1]
    print(NEW_STRING)

def compare_numbers():
    """
    Takes numbers as input and compares if they are larger, smaller or
    the same as the last number the user typed in.
    """
    print("Please enter two numbers for me to compare for you")
    LAST_NUMBER = None  # Declares a variable to compare with the users input.

    while True:
        number = input("Please enter a number: ")
        if number == "done":
            print("Quitting")
            break
        try:
            number = int(number)
        except ValueError:
            print("Not a number")

        if LAST_NUMBER is None:
            LAST_NUMBER = number
            continue

        if number > LAST_NUMBER:
            print("Larger")
        elif number < LAST_NUMBER:
            print("Smaller")
        else:
            print("Same")

        LAST_NUMBER = number  # We now declare last_number to
        # become the users number again so that the number comparison will work correctly.

def calculate_luhna_sum(ssn):
    """
    Calculates the social security number with
    the Luhn-algorithm
    """
    sum_odd_digits = 0
    sum_even_digits = 0

    for digit in ssn[0::2]:
        digit = int(digit) * 2
        if digit >= 10:
            sum_even_digits += 1 + (digit % 10)
        else:
            sum_even_digits += digit

    for digit in ssn[1::2]:
        sum_odd_digits += int(digit)

    total = sum_even_digits + sum_odd_digits
    return total

def validate_ssn():
    """
    Checks if social security number is valid with the Luhn-algorithm
    """
    print("Welcome to the social security number validater.")
    password = input("Please enter your social security number"
                     " (in YY-MM-DD-XXXX format) to check if its valid: ")
    password = password.replace("-", "")
    calc_result = calculate_luhna_sum(password)

    if calc_result % 10 == 0:
        print("Valid")
    else:
        print("Not valid")

def robber_language():
    """
    Takes a string and converts it to robber language
    """
    print("I can speak the robber language!")

    vocals =  ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]

    ROBBER_MESSAGE = ""
    message = input("Enter something you want me to say: ")

    for letter in message:
        if letter in vocals:
            ROBBER_MESSAGE += letter
        else:
            ROBBER_MESSAGE += letter + "o" + letter.lower()
    print(ROBBER_MESSAGE)
    