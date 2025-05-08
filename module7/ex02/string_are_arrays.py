#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    string_are_arrays.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 16:12:55 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 16:12:56 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

parameters = sys.argv[1:]
if not parameters or len(parameters) != 1:
	print("none")
else:
	z_count = 0
	for letter in parameters[0]:
		if letter == 'z':
			z_count += 1
	print('z' * z_count)
