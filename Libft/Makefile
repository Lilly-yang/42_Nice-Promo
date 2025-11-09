# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lyang <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/03 15:28:41 by lyang             #+#    #+#              #
#    Updated: 2025/11/03 15:29:41 by lyang            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libft.a

CC = cc
CFLAGS = -Wall -Wextra -Werror

AR = ar rcs
RM = rm -f


SRCS = ft_*.c
OBJ = $(SRCS:.c=.o)
INCS = libft.h


all: $(NAME)

$(NAME): $(OBJ)
	$(AR) $(NAME) $(OBJS)

%.o: %.c $(INCS)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re