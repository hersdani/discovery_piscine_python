#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    methods_everywhere.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 17:26:32 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 17:26:32 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def shrink(string):
	print(string[0:8])

def enlarge(string):
	while len(string) < 8:
		string += 'Z'
	print(string)

if len(sys.argv) == 1:
	print("none")
else:
	for arg in sys.argv[1:]:
		if len(arg) > 8:
			shrink(arg)
		elif len(arg) == 8:
			print(arg)
		else:
			enlarge(arg)
