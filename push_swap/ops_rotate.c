/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_rotate.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:29 by lyang             #+#    #+#             */
/*   Updated: 2026/07/22 16:27:39 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	rotate(t_stack *stack)
{
	int	i;
	int	first;

	if (!stack || stack->size < 2)
		return ;
	first = stack->arr[0];
	i = 0;
	while (i < stack->size - 1)
	{
		stack->arr[i] = stack->arr[i + 1];
		i++;
	}
	stack->arr[stack->size - 1] = first;
}

static t_bench	*get_bench(t_stack *a, t_stack *b)
{
	if (a && a->bench)
		return (a->bench);
	if (b && b->bench)
		return (b->bench);
	return (NULL);
}

void	op_ra(t_stack *a, int print)
{
	rotate(a);
	if (print && a && a->bench)
		a->bench->ra++;
	if (print && !a->bench->count_only)
		write(1, "ra\n", 3);
}

void	op_rb(t_stack *b, int print)
{
	rotate(b);
	if (print && b && b->bench)
		b->bench->rb++;
	if (print && !b->bench->count_only)
		write(1, "rb\n", 3);
}

void	op_rr(t_stack *a, t_stack *b, int print)
{
	t_bench	*bench;

	bench = get_bench(a, b);
	rotate(a);
	rotate(b);
	if (print && bench)
		bench->rr++;
	if (print && !bench->count_only)
		write(1, "rr\n", 3);
}
