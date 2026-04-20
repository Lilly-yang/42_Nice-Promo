#include "../include/push_swap.h"

static void	swap_top(t_stack *stack)
{
	int	tmp;

	if (!stack || stack->size < 2)
		return ;
	tmp = stack->arr[0];
	stack->arr[0] = stack->arr[1];
	stack->arr[1] = tmp;
}

void	op_sa(t_stack *a, int print)
{
	swap_top(a);
	if (print)
		write(1, "sa\n", 3);
}

void	op_sb(t_stack *b, int print)
{
	swap_top(b);
	if (print)
		write(1, "sb\n", 3);
}

void	op_ss(t_stack *a, t_stack *b, int print)
{
	swap_top(a);
	swap_top(b);
	if (print)
		write(1, "ss\n", 3);
}
