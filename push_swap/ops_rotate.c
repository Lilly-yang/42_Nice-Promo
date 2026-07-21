/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_rotate.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:29 by lyang             #+#    #+#             */
/*   Updated: 2026/06/08 00:55:30 by lyang            ###   ########.fr       */
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

void	op_ra(t_stack *a, int print)
{
	rotate(a);
	if (print)
		write(1, "ra\n", 3);
}

void	op_rb(t_stack *b, int print)
{
	rotate(b);
	if (print)
		write(1, "rb\n", 3);
}

void	op_rr(t_stack *a, t_stack *b, int print)
{
	rotate(a);
	rotate(b);
	if (print)
		write(1, "rr\n", 3);
}
