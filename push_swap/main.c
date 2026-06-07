/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:16 by lyang             #+#    #+#             */
/*   Updated: 2026/06/08 00:55:17 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sort_stack(t_stack *a, t_stack *b)
{
	if (a->size <= 5)
		sort_small(a, b);
	else if (a->size <= 100)
		sort_chunk(a, b);
	else
		sort_radix(a, b);
}

int	main(int argc, char **argv)
{
	t_parse_result	parsed;
	t_stack			a;
	t_stack			b;

	if (argc < 2)
		return (0);
	if (!parse_arguments(argc, argv, &parsed))
		parse_error_exit();
	stack_init(&a, parsed.values, parsed.count);
	stack_init(&b, malloc(sizeof(int) * parsed.count), 0);
	if (!b.arr)
		error_exit(&a, NULL);
	if (!stack_is_sorted(&a))
		sort_stack(&a, &b);
	stack_free(&a);
	stack_free(&b);
	return (0);
}
