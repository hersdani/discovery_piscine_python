#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    advanced_mult.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 11:09:41 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 11:09:41 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

count1 = 0
while count1 <= 10:
	print(f"Table of {count1}:", end="")
	count2 = 0
	while count2 <= 10:
		print(f" {count1 * count2}", end="")
		count2 += 1
	count1 += 1
	print()
