#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    persons_of_interest.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/07 10:56:16 by dherszen          #+#    #+#              #
#    Updated: 2025/05/07 10:56:17 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def get_birth_date(person):
    return person["date_of_birth"]

def famous_births(persons_dict):
    sorted_persons = sorted(persons_dict.values(), key=get_birth_date)
#    print(f"Sorted persons: {sorted_persons}")
    for person in sorted_persons:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")


if __name__ == "__main__":
    women_scientists = {
        "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
        "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
        "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
        "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
    }
    famous_births(women_scientists)
