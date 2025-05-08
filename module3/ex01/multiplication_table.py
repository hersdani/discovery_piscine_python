#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multiplication_table.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 10:46:08 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 10:46:08 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

print("Enter a number")
number_str = input().strip()
if not (number_str.isdigit()) or int(number_str) <= 0:
	print("Error")
	exit(1)
number = int(number_str)
count = 0
while count < 10:
	print(f"{count} x {number} = {count * number}")
	count += 1
