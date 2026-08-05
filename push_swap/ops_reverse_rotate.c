/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_reverse_rotate.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:25 by lyang             #+#    #+#             */
/*   Updated: 2026/07/22 16:27:17 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	reverse_rotate(t_stack *stack)
{
	int	i;
	int	last;

	if (!stack || stack->size < 2)
		return ;
	last = stack->arr[stack->size - 1];
	i = stack->size - 1;
	while (i > 0)
	{
		stack->arr[i] = stack->arr[i - 1];
		i--;
	}
	stack->arr[0] = last;
}

static t_bench	*get_bench(t_stack *a, t_stack *b)
{
	if (a && a->bench)
		return (a->bench);
	if (b && b->bench)
		return (b->bench);
	return (NULL);
}

void	op_rra(t_stack *a, int print)
{
	reverse_rotate(a);
	if (print && a && a->bench)
		a->bench->rra++;
	if (print && !a->bench->count_only)
		write(1, "rra\n", 4);
}

void	op_rrb(t_stack *b, int print)
{
	reverse_rotate(b);
	if (print && b && b->bench)
		b->bench->rrb++;
	if (print && !b->bench->count_only)
		write(1, "rrb\n", 4);
}

void	op_rrr(t_stack *a, t_stack *b, int print)
{
	t_bench	*bench;

	bench = get_bench(a, b);
	reverse_rotate(a);
	reverse_rotate(b);
	if (print && bench)
		bench->rrr++;
	if (print && !bench->count_only)
		write(1, "rrr\n", 4);
}
