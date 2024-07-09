#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
import marvin1
import marvin2
import inventory
import emission_functions

def main():
    """
    Runs functions from the marvin1 module.
    """

    bag = []
    STOP = False
    while not STOP:
        marvin1.menu()

        choice = input(">>> ")

        if choice == "q":
            print("Goodbye, i'm going to bed now.")
            STOP = True

        elif choice == "1":
            marvin1.greet()

        elif choice == "2":
            marvin1.celcius_to_fahrenheit()

        elif choice == "3":
            marvin1.points_to_grade()

        elif choice == "4":
            marvin1.sum_and_average()

        elif choice == "5":
            marvin1.hyphen_string()

        elif choice == "6":
            marvin1.compare_numbers()

        elif choice == "7":
            marvin1.validate_ssn()

        elif choice == "8":
            marvin1.robber_language()

        elif choice == "9":
            birthdate = input("Enter birthdate: ")
            print(marvin2.create_ssn(birthdate))

        elif choice == "10":
            string = input("Type me a name and i'll give you the acronym: ")
            print(marvin2.get_acronym(string))

        elif choice == "11":
            word = input("Type me a word: ")
            print(marvin2.randomize_string(word))

        elif choice == "12":
            string = input("Please enter a string: ")
            sub_str = input("Enter a sub-string: ")
            print(marvin2.find_all_indexes(string, sub_str))

        elif "inv pick" in choice:
            item_list = choice.split(" ")
            inventory.pick(bag, item_list, item_list)

        elif "inv drop" in choice:
            item = choice.split(" ")
            inventory.drop(bag, item)

        elif "inv swap" in choice:
            swap_list = choice.split(" ")
            inventory.swap(bag, swap_list[2], swap_list[3])

        elif "inv" in choice:
            inventory.inv(bag)

        elif choice == "13":
            search_word = input("Enter country name or part of country name to see if it exist: ")
            try:
                found_str = ", ".join(emission_functions.search_country(search_word))
                print(f"Following countries were found: {found_str}")
            except ValueError:
                print("Country does not exist")

        elif choice == "14":
            country, year1, year2 = input("Enter Country,year1,year2: ").split(",")
            try:
                emission_difference = emission_functions.get_country_change_for_years(
                    country,
                    int(year1),
                    int(year2)
                )
                print(f"{country}: {emission_difference:.2f}%")
            except ValueError as e:
                print(str(e))

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        if not STOP:
            input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
