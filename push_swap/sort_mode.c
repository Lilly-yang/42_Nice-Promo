/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_mode.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/15 00:00:00 by ylecain           #+#    #+#             */
/*   Updated: 2026/07/22 17:10:49 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static t_mode	select_adaptive(double disorder)
{
	if (disorder < 0.2)
		return (MODE_SIMPLE);
	if (disorder < 0.5)
		return (MODE_MEDIUM);
	return (MODE_COMPLEX);
}

static void	launch_sort(t_mode mode, t_stack *a, t_stack *b)
{
	if (mode == MODE_SIMPLE)
		sort_small(a, b);
	else if (mode == MODE_MEDIUM)
		sort_chunk(a, b);
	else if (!stack_is_sorted(a))
		sort_radix(a, b);
}

t_mode	run_sort(t_mode mode, t_stack *a, t_stack *b, double disorder)
{
	t_mode	used;

	used = mode;
	if (mode == MODE_ADAPTIVE)
		used = select_adaptive(disorder);
	if (stack_is_sorted(a))
		return (used);
	launch_sort(used, a, b);
	return (used);
}
