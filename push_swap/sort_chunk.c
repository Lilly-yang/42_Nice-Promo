/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_chunk.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:45 by lyang             #+#    #+#             */
/*   Updated: 2026/07/15 00:00:00 by ylecain          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	int_sqrt(int n)
{
	int	root;

	root = 1;
	while ((root + 1) * (root + 1) <= n)
		root++;
	return (root);
}

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

void	sort_chunk(t_stack *a, t_stack *b)
{
	int	n;
	int	chunk_size;
	int	idx;

	if (!compress_values(a))
		error_exit(a, b);
	n = a->size;
	chunk_size = int_sqrt(n);
	if (chunk_size < 1)
		chunk_size = 1;
	fill_chunks(a, b, n, chunk_size);
	while (b->size > 0)
	{
		idx = index_of_max(b);
		bring_max_to_top(b, idx, b->size);
		op_pa(a, b, 1);
	}
}
