#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    your_namebook.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/07 10:15:19 by dherszen          #+#    #+#              #
#    Updated: 2025/05/07 10:15:19 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def array_of_names(name_dict):
    full_names = []
    for first_name, last_name in name_dict.items():
        full_names.append(f"{first_name.capitalize()} {last_name.capitalize()}")
    return full_names

if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))
