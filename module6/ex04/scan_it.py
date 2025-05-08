#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scan_it.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 14:54:18 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 14:54:19 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re, sys

parameters = sys.argv[1:]
if not parameters or len(parameters) < 2:
	print("none")
	exit(0)
occurances = len(re.findall(parameters[0], parameters[1]))
if occurances == 0:
	print("none")
else:
	print(occurances)
