#include "../include/push_swap.h"

static int	parse_int_strict(const char *s, int *out)
{
	long	value;
	int		sign;
	int		i;

	if (!s || !*s)
		return (0);
	i = 0;
	sign = 1;
	if (s[i] == '+' || s[i] == '-')
	{
		if (s[i] == '-')
			sign = -1;
		i++;
	}
	if (!s[i])
		return (0);
	value = 0;
	while (s[i])
	{
		if (s[i] < '0' || s[i] > '9')
			return (0);
		value = value * 10 + (s[i] - '0');
		if ((sign == 1 && value > INT_MAX) || (sign == -1 && -value < INT_MIN))
			return (0);
		i++;
	}
	*out = (int)(value * sign);
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
		if (!parse_int_strict(tokens[i], &value) || !append_value(arr, size, value))
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
		if (!argv[i] || !*argv[i])
		{
			free(values);
			return (0);
		}
		if (!parse_one_arg(argv[i], &values, &size))
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
