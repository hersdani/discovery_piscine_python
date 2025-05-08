#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    password.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/05 17:19:27 by dherszen          #+#    #+#              #
#    Updated: 2025/05/05 17:19:28 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

password = "Python is awesome"
user_input = input().strip()
if user_input == password:
	print("ACCESS GRANTED")
else:
	print("ACCESS DENIED")
