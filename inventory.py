"""
En modul med funktioner för att användaren
ska kunna använda en lista/ryggsäck med viss
funktionalitet.
"""

def pick(bag, thing, position):
    """
    Picks an item and puts it in the bag 
    with an optional position.
    """
    try:
        user_index = int(position[3])
        bag.insert(user_index, thing[2])
        print(f'"{thing[2]}" has been added on index "{position[3]}".')
    except IndexError:
        bag.append(thing[2])
        print(f'"{thing[2]}" has been added')
    return bag

def inv(bag):
    """
    Prints the number of items in the bag
    and all the contents of the bag.
    """
    nr_of_items = len(bag)

    message = f"Bagpack has {nr_of_items} items: {bag}"
    print(message)

def drop(bag, item):
    """
    Removes a user-specified item from the bag.
    """
    if item[2] in bag:
        bag.remove(item[2])
        print(f"{item[2]} has been removed.")
    else:
        print(f'Error! I have no "{item[2]}" in the bagpack.')

    return bag

def swap(bag, item_one, item_two):
    """
    Swaps two items in the bag list
    """
    try:
        a, b = bag.index(item_two), bag.index(item_one)
        bag[b], bag[a] = bag[a], bag[b]
        print(f'"{item_one}" and "{item_two}" has been swaped.')
    except ValueError:
        print(f'Error! I have no "{item_one}" or "{item_two}" in the bagpack.')
    return bag
