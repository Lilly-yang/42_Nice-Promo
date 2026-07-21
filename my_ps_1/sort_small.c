/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_small.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:50 by lyang             #+#    #+#             */
/*   Updated: 2026/06/08 00:55:51 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	index_of_min(const t_stack *a)
{
	int	i;
	int	idx;

	i = 1;
	idx = 0;
	while (i < a->size)
	{
		if (a->arr[i] < a->arr[idx])
			idx = i;
		i++;
	}
	return (idx);
}

static void	sort_three(t_stack *a)
{
	int	x;
	int	y;
	int	z;

	x = a->arr[0];
	y = a->arr[1];
	z = a->arr[2];
	if (x > y && y < z && x < z)
		op_sa(a, 1);
	else if (x > y && y > z)
	{
		op_sa(a, 1);
		op_rra(a, 1);
	}
	else if (x > y && y < z && x > z)
		op_ra(a, 1);
	else if (x < y && y > z && x < z)
	{
		op_sa(a, 1);
		op_ra(a, 1);
	}
	else if (x < y && y > z && x > z)
		op_rra(a, 1);
}

void	sort_small(t_stack *a, t_stack *b)
{
	int	min_idx;

	if (a->size == 2)
	{
		if (a->arr[0] > a->arr[1])
			op_sa(a, 1);
		return ;
	}
	while (a->size > 3)
	{
		min_idx = index_of_min(a);
		if (min_idx <= a->size / 2)
			while (min_idx-- > 0)
				op_ra(a, 1);
		else
			while (min_idx++ < a->size)
				op_rra(a, 1);
		op_pb(a, b, 1);
	}
	if (!stack_is_sorted(a))
		sort_three(a);
	while (b->size > 0)
		op_pa(a, b, 1);
}
