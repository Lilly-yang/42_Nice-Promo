/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:38 by lyang             #+#    #+#             */
/*   Updated: 2026/06/08 01:01:53 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	parse_int_strict(const char *s, int *out)
{
	char	*end;
	long	value;

	if (!s || !*s)
		return (0);
	if (*s == ' ' || *s == '\t' || *s == '\n' || *s == '\v'
		|| *s == '\f' || *s == '\r')
		return (0);
	value = strtol(s, &end, 10);
	if (*end || value < INT_MIN || value > INT_MAX)
		return (0);
	*out = (int)value;
	return (1);
}

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

static int	append_value(int **arr, int *size, int value)
{
	int	*new_arr;
	int	i;

	if (has_duplicate(*arr, *size, value))
		return (0);
	new_arr = malloc(sizeof(int) * (*size + 1));
	if (!new_arr)
		return (0);
	i = 0;
	while (i < *size)
	{
		new_arr[i] = (*arr)[i];
		i++;
	}
	new_arr[*size] = value;
	free(*arr);
	*arr = new_arr;
	(*size)++;
	return (1);
}

static int	parse_one_arg(const char *arg, int **arr, int *size)
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
			|| !append_value(arr, size, value))
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
	int	i;

	values = NULL;
	size = 0;
	i = 1;
	while (i < argc)
	{
		if (!argv[i] || !*argv[i] || !parse_one_arg(argv[i], &values, &size))
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
