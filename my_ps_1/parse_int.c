/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_int.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ylecain <ylecain@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/09 00:00:00 by ylecain           #+#    #+#             */
/*   Updated: 2026/07/15 00:00:00 by ylecain          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	is_digit(char c)
{
	return (c >= '0' && c <= '9');
}

static int	out_of_range(long val, int sign)
{
	if (sign == 1 && val > INT_MAX)
		return (1);
	if (sign == -1 && val > 2147483648L)
		return (1);
	return (0);
}

static int	parse_sign(const char **s)
{
	int	sign;

	sign = 1;
	while (is_space(**s))
		(*s)++;
	if (**s == '-' || **s == '+')
	{
		if (**s == '-')
			sign = -1;
		(*s)++;
	}
	return (sign);
}

int	parse_int_strict(const char *s, int *out)
{
	long	val;
	int		sign;

	val = 0;
	if (!s || !*s)
		return (0);
	sign = parse_sign(&s);
	if (!is_digit(*s))
		return (0);
	while (is_digit(*s))
	{
		val = val * 10 + (*s - '0');
		if (out_of_range(val, sign))
			return (0);
		s++;
	}
	if (*s != '\0')
		return (0);
	*out = (int)(val * sign);
	return (1);
}
