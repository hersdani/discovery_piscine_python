#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    isneg.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/05 17:12:51 by dherszen          #+#    #+#              #
#    Updated: 2025/05/05 17:12:51 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

number_str = input().strip()
if number_str.isdigit() or (number_str[0] == '-' and number_str[1:].isdigit()):
	number = int(number_str)
else:
	print("Invalid input. Please enter a valid number.")
	exit(1)
if number == 0:
	print("This number is both positive and negative.")
elif number < 0:
	print("This number is negative.")
else:
	print("This number is positive.")
