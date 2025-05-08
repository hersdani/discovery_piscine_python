#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/06 12:50:20 by dherszen          #+#    #+#              #
#    Updated: 2025/05/06 12:50:20 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
# the 2 lines below are unnecessary, as a set has already unique values
#new_array = []
#[new_array.append(x) for x in original_array if x not in new_array]
new_set = {x + 2 for x in original_array if x > 5}
print(original_array)
print(new_set)
