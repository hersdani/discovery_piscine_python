#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count_it.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 15:27:58 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 15:27:58 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

parameters = sys.argv[1:]
if not parameters:
	print("none")
else:
	print(f"parameters: {len(parameters)}")
	for param in parameters:
		print(f"{param}: {len(param)}")
