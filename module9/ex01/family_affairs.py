#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    family_affairs.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/07 10:25:29 by dherszen          #+#    #+#              #
#    Updated: 2025/05/07 10:25:29 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def find_the_redheads(family_members_dict):
    """
    Takes a dictionary of family members (keys) and their hair colors (values).
    Returns a list of first names of individuals with red hair.
    Uses filter(), dict.keys(), and numpy's tolist() method.
    """
    def has_red_hair(name):
        # Helper function to check for red hair.
        # It's defined inside find_the_redheads to have access to family_members_dict.
        return family_members_dict.get(name) == "red"

    # 1. Use .keys() to get an iterable of names (keys from the dictionary).
    names_iterable = family_members_dict.keys()

#    for name in names_iterable:
#        print(name)  # Print each name for debugging purposes.
    # 2. Use filter() with the helper function to get an iterator
    #    containing only the names of redheads.
    redheads_iterator = filter(has_red_hair, names_iterable)

    # 3. Convert the iterator to a Python list first.
    #    This step explicitly consumes the iterator.
    list_of_redheads_from_iterator = list(redheads_iterator)
#    print(f"list_of_redheads_from_iterator: {list_of_redheads_from_iterator}")
    # Convert the Python list to a NumPy array.
    # If list_of_redheads_from_iterator is empty, np.array([]) is created.
    numpy_array_of_redheads = np.array(list_of_redheads_from_iterator)
#    print(f"numpy_array_of_redheads: {numpy_array_of_redheads}")
    # 4. Use .tolist() from the NumPy array to get a Python list.
    #    If numpy_array_of_redheads is empty, .tolist() returns an empty list [].
    return numpy_array_of_redheads.tolist()

if __name__ == "__main__":
	dupont_family = {
		"florian": "red",
		"marie": "blond",
		"virginie": "brunette",
		"david": "red",
		"franck": "red"
	}
	print(find_the_redheads(dupont_family))
