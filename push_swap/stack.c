/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:56 by lyang             #+#    #+#             */
/*   Updated: 2026/06/08 00:55:57 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	stack_init(t_stack *stack, int *values, int size)
{
	stack->arr = values;
	stack->size = size;
}

void	stack_free(t_stack *stack)
{
	if (!stack)
		return ;
	free(stack->arr);
	stack->arr = NULL;
	stack->size = 0;
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
