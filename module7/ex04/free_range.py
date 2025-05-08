#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    free_range.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 16:39:02 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 16:39:02 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

parameters = sys.argv[1:]
if len(parameters) != 2:
	print("none")
else:
	array = list(range(int(parameters[0]), int(parameters[1]) + 1))
	print(array)
