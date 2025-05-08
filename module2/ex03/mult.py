#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mult.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/05 17:25:02 by dherszen          #+#    #+#              #
#    Updated: 2025/05/05 17:25:03 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

print("Enter the first number: ")
number_str = input().strip()
if number_str.isdigit() or (number_str[0] == '-' and number_str[1:].isdigit()):
	number1 = int(number_str)
else:
	print("Invalid input. Please enter a valid number.")
	exit(1)
print("Enter the second number: ")
number_str = input().strip()
if number_str.isdigit() or (number_str[0] == '-' and number_str[1:].isdigit()):
	number2 = int(number_str)
else:
	print("Invalid input. Please enter a valid number.")
	exit(1)
result = number1 * number2
print(f"{number1} x {number2} = {result}")
if result == 0:
	print("This result is positive and negative.")
elif result < 0:
	print("The result is negative.")
else:
	print("The result is positive.")
