#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parameter_matching.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 15:21:19 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 15:21:19 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

parameters = sys.argv[1:]
if not parameters or len(parameters) != 1:
	print("none")
else:
	input_str = input("What was the parameter? ")
	if input_str == parameters[0]:
		print("Good job!")
	else:
		print("Nope, sorry...")
