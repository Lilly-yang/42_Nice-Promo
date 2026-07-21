/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:53 by lyang             #+#    #+#             */
/*   Updated: 2026/06/08 00:55:54 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	sort_ints(int *arr, int n)
{
	int	i;
	int	j;
	int	tmp;

	i = 0;
	while (i < n - 1)
	{
		j = 0;
		while (j < n - 1 - i)
		{
			if (arr[j] > arr[j + 1])
			{
				tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
			j++;
		}
		i++;
	}
}

static int	find_index(const int *arr, int n, int value)
{
	int	i;

	i = 0;
	while (i < n)
	{
		if (arr[i] == value)
			return (i);
		i++;
	}
	return (-1);
}

int	compress_values(t_stack *a)
{
	int	*sorted;
	int	i;
	int	idx;

	sorted = malloc(sizeof(int) * a->size);
	if (!sorted)
		return (0);
	ft_memmove(sorted, a->arr, sizeof(int) * a->size);
	sort_ints(sorted, a->size);
	i = 0;
	while (i < a->size)
	{
		idx = find_index(sorted, a->size, a->arr[i]);
		if (idx < 0)
			return (free(sorted), 0);
		a->arr[i] = idx;
		i++;
	}
	free(sorted);
	return (1);
}

int	index_of_max(const t_stack *stack)
{
	int	i;
	int	idx;

	i = 1;
	idx = 0;
	while (i < stack->size)
	{
		if (stack->arr[i] > stack->arr[idx])
			idx = i;
		i++;
	}
	return (idx);
}
