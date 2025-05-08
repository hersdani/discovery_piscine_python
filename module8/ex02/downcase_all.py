#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    downcase_all.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 16:59:18 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 16:59:19 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def downcase_it(string):
	return string.lower()

if len(sys.argv) > 1:
	for arg in sys.argv[1:]:
		print(downcase_it(arg))
else:
	print("none")
