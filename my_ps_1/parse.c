/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ylecain <ylecain@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:38 by lyang             #+#    #+#             */
/*   Updated: 2026/07/09 00:00:00 by ylecain          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	has_duplicate(int *arr, int size, int value)
{
	int	i;

	i = 0;
	while (i < size)
	{
		if (arr[i] == value)
			return (1);
		i++;
	}
	return (0);
}

static int	grow_values(int **arr, int size, int *capacity)
{
	int	*new_arr;
	int	new_capacity;
	int	i;

	if (*capacity == 0)
		new_capacity = 16;
	else
		new_capacity = *capacity * 2;
	new_arr = malloc(sizeof(int) * new_capacity);
	if (!new_arr)
		return (0);
	i = 0;
	while (i < size)
	{
		new_arr[i] = (*arr)[i];
		i++;
	}
	free(*arr);
	*arr = new_arr;
	*capacity = new_capacity;
	return (1);
}

static int	append_value(int **arr, int *size, int *capacity, int value)
{
	if (has_duplicate(*arr, *size, value))
		return (0);
	if (*size == *capacity && !grow_values(arr, *size, capacity))
		return (0);
	(*arr)[*size] = value;
	(*size)++;
	return (1);
}

static int	parse_one_arg(const char *arg, int **arr, int *size, int *capacity)
{
	char	**tokens;
	int		value;
	int		i;
	int		parsed_any;

	tokens = split_whitespaces(arg);
	if (!tokens)
		return (0);
	i = 0;
	parsed_any = 0;
	while (tokens[i])
	{
		if (!parse_int_strict(tokens[i], &value)
			|| !append_value(arr, size, capacity, value))
		{
			free_tokens(tokens);
			return (0);
		}
		parsed_any = 1;
		i++;
	}
	free_tokens(tokens);
	return (parsed_any);
}

int	parse_arguments(int argc, char **argv, t_parse_result *out)
{
	int	*values;
	int	size;
	int	capacity;
	int	i;

	values = NULL;
	size = 0;
	capacity = 0;
	i = 1;
	while (i < argc)
	{
		if (!argv[i] || !*argv[i]
			|| !parse_one_arg(argv[i], &values, &size, &capacity))
		{
			free(values);
			return (0);
		}
		i++;
	}
	out->values = values;
	out->count = size;
	return (size > 0);
}
