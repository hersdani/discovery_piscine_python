#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    help_your_professor.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/07 10:53:34 by dherszen          #+#    #+#              #
#    Updated: 2025/05/07 10:53:34 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def average(scores_dict):
	scores = scores_dict.values()
	total_score = sum(scores)
	number_of_students = len(scores)
	return total_score / number_of_students

if __name__ == "__main__":
	class_3B = {
		"marine": 18,
		"jean": 15,
		"coline": 8,
		"luc": 9
	}
	class_3C = {
		"quentin": 17,
		"julie": 15,
		"marc": 8,
		"stephanie": 13
	}
	print(f"Average for class 3B: {average(class_3B)}.")
	print(f"Average for class 3C: {average(class_3C)}.")
