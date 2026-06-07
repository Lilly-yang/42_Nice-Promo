/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_radix.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:47 by lyang             #+#    #+#             */
/*   Updated: 2026/06/08 00:55:48 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	get_max_bits(int n)
{
	int	max_bits;

	max_bits = 0;
	while (((n - 1) >> max_bits) != 0)
		max_bits++;
	return (max_bits);
}

static void	process_bit(t_stack *a, t_stack *b, int n, int bit)
{
	int	i;

	i = 0;
	while (i < n)
	{
		if (((a->arr[0] >> bit) & 1) == 0)
			op_pb(a, b, 1);
		else
			op_ra(a, 1);
		i++;
	}
	while (b->size > 0)
		op_pa(a, b, 1);
}

void	sort_radix(t_stack *a, t_stack *b)
{
	int	max_bits;
	int	bit;
	int	n;

	if (!compress_values(a))
		error_exit(a, b);
	n = a->size;
	max_bits = get_max_bits(n);
	bit = 0;
	while (bit < max_bits)
		process_bit(a, b, n, bit++);
}
