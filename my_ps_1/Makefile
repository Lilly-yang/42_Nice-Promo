NAME		=	push_swap
CC			=	cc
CFLAGS		=	-Wall -Wextra -Werror
INCLUDES	=	-I.
HEADER		=	push_swap.h
COMMON_SRCS	=	parse.c \
				parse_int.c \
				parse_mode.c \
				parse_split.c \
				stack.c \
				ops_swap.c \
				ops_push.c \
				ops_rotate.c \
				ops_reverse_rotate.c \
				utils.c \
				sort_utils.c \
				error.c \
				disorder.c \
				bench.c \
				bench_report.c \
				bench_counts.c \
				sort_mode.c
PUSH_SRCS	=	main.c \
				sort_small.c \
				sort_chunk.c \
				sort_radix.c
COMMON_OBJS	=	$(COMMON_SRCS:.c=.o)
PUSH_OBJS	=	$(PUSH_SRCS:.c=.o)

all: $(NAME)

$(NAME): $(COMMON_OBJS) $(PUSH_OBJS)
	$(CC) $(CFLAGS) $(COMMON_OBJS) $(PUSH_OBJS) -o $(NAME)

%.o: %.c $(HEADER)
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -f $(COMMON_OBJS) $(PUSH_OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
