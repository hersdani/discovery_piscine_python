#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    iszero.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/05 16:59:52 by dherszen          #+#    #+#              #
#    Updated: 2025/05/05 17:10:06 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

number_str = input().strip()
if number_str.isdigit():
	number = int(number_str)
else:
	print("Invalid input. Please enter a valid number.")
	exit(1)
if number == 0:
	print("This number is equal to zero.")
else:
	print("This number is different from zero.")
