NAME		=	push_swap
CC			=	cc
CFLAGS		=	-Wall -Wextra -Werror
INCLUDES	=	-Iinclude

COMMON_SRCS	=	src/parse.c \
				src/parse_split.c \
				src/stack.c \
				src/ops_swap.c \
				src/ops_push.c \
				src/ops_rotate.c \
				src/ops_reverse_rotate.c \
				src/utils.c \
				src/error.c

PUSH_SRCS	=	src/main.c \
				src/sort_small.c \
				src/sort_radix.c

PUSH_OBJS	=	$(COMMON_SRCS:.c=.o) $(PUSH_SRCS:.c=.o)

all: $(NAME)

$(NAME): $(PUSH_OBJS)
	$(CC) $(CFLAGS) $(PUSH_OBJS) -o $(NAME)

%.o: %.c include/push_swap.h
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -f $(PUSH_OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all bonus clean fclean re
