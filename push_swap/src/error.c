#include "../include/push_swap.h"

void	parse_error_exit(void)
{
	write(2, "Error\n", 6);
	exit(1);
}

void	error_exit(t_stack *a, t_stack *b)
{
	if (a)
		stack_free(a);
	if (b)
		stack_free(b);
	write(2, "Error\n", 6);
	exit(1);
}
