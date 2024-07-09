"""
Marvin2 docstring
"""

import math
import random
import marvin1

def create_ssn(birthdate):
    """
    Creates a social security number with calculate_luhna_sum()
    """
    birthdate = birthdate.replace("-", "")
    random_value = random.randint(100, 999)
    ssn = str(birthdate) + str(random_value)

    marvin1.calculate_luhna_sum(ssn)
    next_highest_tens = math.ceil(marvin1.calculate_luhna_sum(ssn) / 10) * 10
    last_number = next_highest_tens - marvin1.calculate_luhna_sum(ssn)
    new_ssn = ssn + str(last_number)
    new_ssn = new_ssn[:6] + '-' + new_ssn[6:]
    return new_ssn

def get_acronym(string):
    """
    Takes a name and gives back the acronym
    """
    new_string = ""
    for letter in string:
        if letter.isupper():
            new_string += letter
        else:
            continue
    return new_string

def randomize_string(word):
    """
    randomizes a string and outputs it.
    """
    random_word = ''.join(random.sample(word,len(word)))

    final_string = f"{word} --> {random_word}"
    return final_string

def find_all_indexes(string, sub_str):
    """
    Takes input for a string and sub-string
    and finds where the sub-string occurs in the
    given string.
    """
    start_index = 0
    string_index = ""

    while True:
        try:
            index = string.index(sub_str, start_index)
            start_index = index + 1
            string_index += str(index) + ","
        except ValueError:
            break
    string_index = string_index[:-1:]

    return string_index
    