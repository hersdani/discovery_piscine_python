#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    to25.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/05 18:45:29 by dherszen          #+#    #+#              #
#    Updated: 2025/05/05 18:45:29 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

print("Enter a number less than 25")
number_str = input().strip()
if not (number_str.isdigit() or (number_str[0] == '-' and number_str[1:].isdigit())) or int(number_str) > 25:
	print("Error")
	exit(1)
number = int(number_str)
while number <= 25:
	print(f"Inside the loop, my variable is {number}")
	number += 1
