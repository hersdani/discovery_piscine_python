#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    downcase_it.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 13:39:47 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 13:39:47 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
parameter = sys.argv[1:]
if not parameter or len(parameter) > 1:
	print("none")
else:
	print(parameter[0].lower())
