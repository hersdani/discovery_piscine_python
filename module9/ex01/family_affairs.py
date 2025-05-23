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

def find_the_redheads(family_members_dict):
    def has_red_hair(name):
        return family_members_dict.get(name) == "red"

    redheads_iterator = filter(has_red_hair, family_members_dict.keys())
    return list(redheads_iterator)

if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))

"""
import numpy as np

def find_the_redheads(family_members_dict):
    def has_red_hair(name):
        return family_members_dict.get(name) == "red"

    names_iterable = family_members_dict.keys()
    redheads_iterator = filter(has_red_hair, names_iterable)
    list_of_redheads_from_iterator = list(redheads_iterator)
    numpy_array_of_redheads = np.array(list_of_redheads_from_iterator)
    return numpy_array_of_redheads.tolist()
"""
