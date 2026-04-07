# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/19 11:26:13 by lyang             #+#    #+#              #
#    Updated: 2026/04/03 10:03:51 by lyang            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libftprintf.a

CFLAGS = -Wall -Wextra -Werror

SRC = ft_printf.c ft_printf_sub.c ft_put_out.c ft_putnbr_out.c
OBJ = $(SRC:.c=.o)
INC = ft_printf.h

$(NAME): $(OBJ) $(INC)
	ar rcs $(NAME) $(OBJ)

all: $(NAME)

clean:
	rm -f $(OBJ)
	
fclean: clean
	rm -f $(NAME)
	
re: fclean all