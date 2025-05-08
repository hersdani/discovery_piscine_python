#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    greetings_for_all.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 16:59:18 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 16:59:19 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def greetings(name="noble stranger"):
	if not isinstance(name, str):
		print("Error! It was not a name.")
	else:
		print(f"Hello, {name}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
