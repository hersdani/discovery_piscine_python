#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    append_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 16:34:12 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 16:34:12 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

parameters = sys.argv[1:]
if not parameters:
	print("none")
else:
	for param in parameters:
		if not re.search(r"ism$", param):
			print(f"{param}ism")
