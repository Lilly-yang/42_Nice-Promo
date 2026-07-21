/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_swap.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:32 by lyang             #+#    #+#             */
/*   Updated: 2026/07/09 00:00:00 by ylecain          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	swap_top(t_stack *stack)
{
	int	tmp;

	if (!stack || stack->size < 2)
		return ;
	tmp = stack->arr[0];
	stack->arr[0] = stack->arr[1];
	stack->arr[1] = tmp;
}

static t_bench	*get_bench(t_stack *a, t_stack *b)
{
	if (a && a->bench)
		return (a->bench);
	if (b && b->bench)
		return (b->bench);
	return (NULL);
}

void	op_sa(t_stack *a, int print)
{
	swap_top(a);
	if (print && a && a->bench)
		a->bench->sa++;
	if (print)
		write(1, "sa\n", 3);
}

void	op_sb(t_stack *b, int print)
{
	swap_top(b);
	if (print && b && b->bench)
		b->bench->sb++;
	if (print)
		write(1, "sb\n", 3);
}

void	op_ss(t_stack *a, t_stack *b, int print)
{
	t_bench	*bench;

	bench = get_bench(a, b);
	swap_top(a);
	swap_top(b);
	if (print && bench)
		bench->ss++;
	if (print)
		write(1, "ss\n", 3);
}
