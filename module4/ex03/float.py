#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    float.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 11:52:12 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 11:52:12 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

input_str = input("Give me a number: ")
if (float(input_str).is_integer()):
	print("This number is an integer.")
else:
	print("This number is a decimal.")
