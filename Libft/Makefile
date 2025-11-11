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


SRCS = \
	ft_atoi.c \
	ft_itoa.c \
	ft_putendl_fd.c \
	ft_strlcat.c \
	ft_substr.c \
	ft_bzero.c \
	ft_memchr.c \
	ft_putnbr_fd.c \
	ft_strlcpy.c \
	ft_tolower.c \
	ft_calloc.c \
	ft_memcmp.c \
	ft_putstr_fd.c \
	ft_strlen.c \
	ft_toupper.c \
	ft_isalnum.c \
	ft_memcpy.c \
	ft_split.c \
	ft_strmapi.c \
	ft_isalpha.c \
	ft_memmove.c \
	ft_strchr.c \
	ft_strncmp.c \
	ft_isascii.c \
	ft_memset.c \
	ft_strdup.c \
	ft_strnstr.c \
	ft_isdigit.c \
	ft_striteri.c \
	ft_strrchr.c \
	ft_isprint.c \
	ft_putchar_fd.c \
	ft_strjoin.c \
	ft_strtrim.c
OBJS = $(SRCS:.c=.o)
INCS = libft.h


all: $(NAME)

$(NAME): $(OBJS)
	$(AR) $(NAME) $(OBJS)

%.o: %.c $(INCS)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re