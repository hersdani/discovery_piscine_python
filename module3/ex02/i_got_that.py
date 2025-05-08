#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    i_got_that.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 10:51:14 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 10:51:14 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

input_str = input("What you gotta say? : ").strip()
while input_str != "STOP":
	input_str = input("I got that! Anything else? : ").strip()

"""
first_question = True
while 42:
	if first_question:
		input_str = input("What you gotta say? : ").strip()
		first_question = False
	else:
		input_str = input("I got that! Anything else? : ").strip()
	if input_str == "STOP":
		break
"""
