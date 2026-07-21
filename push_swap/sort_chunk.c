/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_chunk.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:45 by lyang             #+#    #+#             */
/*   Updated: 2026/06/08 01:01:53 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	bring_max_to_top(t_stack *b, int idx, int size)
{
	if (idx <= size / 2)
	{
		while (idx-- > 0)
			op_rb(b, 1);
	}
	else
	{
		while (idx++ < size)
			op_rrb(b, 1);
	}
}

static void	push_chunk(t_stack *a, t_stack *b, int lower, int upper)
{
	int	pushed;
	int	limit;
	int	half;

	limit = upper - lower + 1;
	half = lower + (limit / 2);
	pushed = 0;
	while (pushed < limit && a->size > 0)
	{
		if (a->arr[0] >= lower && a->arr[0] <= upper)
		{
			op_pb(a, b, 1);
			pushed++;
			if (b->size > 1 && b->arr[0] < half)
				op_rb(b, 1);
		}
		else
			op_ra(a, 1);
	}
}

static void	fill_chunks(t_stack *a, t_stack *b, int n, int chunk_size)
{
	int	lower;
	int	upper;

	lower = 0;
	while (lower < n)
	{
		upper = lower + chunk_size - 1;
		if (upper >= n)
			upper = n - 1;
		push_chunk(a, b, lower, upper);
		lower = upper + 1;
	}
}

static void	push_back_sorted(t_stack *a, t_stack *b)
{
	int	idx;

	while (b->size > 0)
	{
		idx = index_of_max(b);
		bring_max_to_top(b, idx, b->size);
		op_pa(a, b, 1);
	}
}

void	sort_chunk(t_stack *a, t_stack *b)
{
	int	n;
	int	chunk_size;

	if (!compress_values(a))
		error_exit(a, b);
	n = a->size;
	if (n <= 100)
		chunk_size = (n + 5 - 1) / 5;
	else
		chunk_size = (n + 11 - 1) / 11;
	fill_chunks(a, b, n, chunk_size);
	push_back_sorted(a, b);
}
