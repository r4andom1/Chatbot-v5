"""
Functions for emissions.
"""
import emission_data as ea

def search_country(search_word):
    """
    Loops over 'Emission_data' and searches after
    countries. If they don't exist an ValueError is
    raised.
    """
    found_countries = []
    for country_name in ea.country_data:
        if search_word.lower() in country_name.lower():
            found_countries.append(country_name.capitalize())
    if not found_countries:
        raise ValueError("Country does not exist!")
    return found_countries

def get_country_year_data_megaton(country, year):
    """
    Collects the CO2 data from a country
    in a specific year.
    """
    emissions_data = {
        1990: ea.emission_1990,
        2005: ea.emission_2005,
        2017: ea.emission_2017
    }

    if year in emissions_data:
        if country.capitalize() in ea.country_data:
            id_nr = ea.country_data[country.capitalize()]["id"]
        else:
            raise ValueError("Country does not exist!")
    else:
        raise ValueError("Wrong year!")

    emissions_year = emissions_data[year].get(id_nr)
    emissions_tons = emissions_year * 1000000
    return emissions_tons

def get_country_change_for_years(country, year1, year2):
    """
    Calculates and compares the CO2 emissions
    of a country between two years.
    """
    emissions_year1 = get_country_year_data_megaton(country, year1)
    emissions_year2 = get_country_year_data_megaton(country, year2)
    return calculate_percentage_difference(emissions_year1, emissions_year2)

def calculate_percentage_difference(old_value, new_value):
    """
    Calculate the percentage difference between two numbers.
    """
    difference = new_value - old_value
    percentage_difference = (difference / old_value) * 100
    return percentage_difference
