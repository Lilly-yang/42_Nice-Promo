NAME		=	push_swap
CC			=	cc
CFLAGS		=	-Wall -Wextra -Werror
INCLUDES	=	-Iinclude

COMMON_SRCS	=	parse.c \
				parse_split.c \
				stack.c \
				ops_swap.c \
				ops_push.c \
				ops_rotate.c \
				ops_reverse_rotate.c \
				utils.c \
				error.c

PUSH_SRCS	=	main.c \
				sort_small.c \
				sort_chunk.c \
				sort_radix.c

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

.PHONY: all clean fclean re
