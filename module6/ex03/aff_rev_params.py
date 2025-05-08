#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_first_param.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 13:24:50 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 13:24:50 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
parameters = sys.argv[1:]
if not parameters or len(parameters) < 2:
	print("none")
	exit(0)
index = len(parameters) - 1
while index >= 0:
	print(parameters[index])
	index -= 1
