# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatsyourname.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/05 15:01:25 by dherszen          #+#    #+#              #
#    Updated: 2025/05/05 16:12:02 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

first_name = input("Hey, what's your first name? : ").strip()
last_name = input("And your last name? : ").strip()
whole_name = first_name + " " + last_name
print(f"Well, pleased to meet you, {whole_name}")
