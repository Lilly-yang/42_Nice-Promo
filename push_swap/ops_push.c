/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_push.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:22 by lyang             #+#    #+#             */
/*   Updated: 2026/06/08 00:55:23 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	push_top(t_stack *dst, t_stack *src)
{
	int	i;
	int	value;

	if (!src || src->size == 0)
		return ;
	value = src->arr[0];
	i = 0;
	while (i < src->size - 1)
	{
		src->arr[i] = src->arr[i + 1];
		i++;
	}
	src->size--;
	i = dst->size;
	while (i > 0)
	{
		dst->arr[i] = dst->arr[i - 1];
		i--;
	}
	dst->arr[0] = value;
	dst->size++;
}

void	op_pa(t_stack *a, t_stack *b, int print)
{
	push_top(a, b);
	if (print)
		write(1, "pa\n", 3);
}

void	op_pb(t_stack *a, t_stack *b, int print)
{
	push_top(b, a);
	if (print)
		write(1, "pb\n", 3);
}
