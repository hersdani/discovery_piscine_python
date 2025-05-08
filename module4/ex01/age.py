#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    age.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 11:31:57 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 11:31:57 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

age = int(input("Enter your age: "))
if age < 0 or age > 120:
	print("Invalid age. Please enter a valid age between 0 and 120.")
	exit(1)
print(f"You are currently {age} years old.")
print(f"In 10 years, you will be {age + 10} years old.")
print(f"In 20 years, you will be {age + 20} years old.")
print(f"In 30 years, you will be {age + 30} years old.")
