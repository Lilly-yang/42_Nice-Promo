/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:56 by lyang             #+#    #+#             */
/*   Updated: 2026/07/09 00:00:00 by ylecain          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	stack_init(t_stack *stack, int *values, int size, t_bench *bench)
{
	stack->arr = values;
	stack->size = size;
	stack->bench = bench;
}

void	stack_free(t_stack *stack)
{
	if (!stack)
		return ;
	free(stack->arr);
	stack->arr = NULL;
	stack->size = 0;
	stack->bench = NULL;
}

int	stack_is_sorted(const t_stack *stack)
{
	int	i;

	if (!stack || stack->size < 2)
		return (1);
	i = 0;
	while (i < stack->size - 1)
	{
		if (stack->arr[i] > stack->arr[i + 1])
			return (0);
		i++;
	}
	return (1);
}
