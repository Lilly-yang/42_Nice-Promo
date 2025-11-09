/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_convert_base.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yourlogin <you@42.fr>                      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/26 00:00:00 by yourlogin         #+#    #+#             */
/*   Updated: 2025/09/26 00:00:00 by yourlogin        ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

static int		ft_strlen(char *s)
{
	int	i;

	i = 0;
	while (s && s[i])
		i++;
	return (i);
}

static int		is_space(char c)
{
	return (c == ' ' || (c >= 9 && c <= 13));
}

static int		base_is_valid(char *base)
{
	int i;
	int j;

	if (!base || ft_strlen(base) < 2)
		return (0);
	i = 0;
	while (base[i])
	{
		if (base[i] == '+' || base[i] == '-' || is_space(base[i]))
			return (0);
		j = i + 1;
		while (base[j])
		{
			if (base[i] == base[j])
				return (0);
			j++;
		}
		i++;
	}
	return (1);
}

static int		index_in_base(char c, char *base)
{
	int i;

	i = 0;
	while (base[i])
	{
		if (base[i] == c)
			return (i);
		i++;
	}
	return (-1);
}

/* Parses like ft_atoi, but with a custom base. Assumes base is valid. */
static int		ft_atoi_base(char *str, char *base)
{
	long	result;
	int		sign;
	int		b;
	int		idx;

	if (!str || !base_is_valid(base))
		return (0);
	b = ft_strlen(base);
	result = 0;
	while (*str && is_space(*str))
		str++;
	sign = 1;
	while (*str == '+' || *str == '-')
	{
		if (*str == '-')
			sign = -sign;
		str++;
	}
	while (*str)
	{
		idx = index_in_base(*str, base);
		if (idx < 0)
			break ;
		result = result * b + idx;
		str++;
	}
	return ((int)(result * sign));
}

/* --- from ft_convert_base2.c --- */
char	*ft_itoa_base_int(int nbr, char *base);

char	*ft_convert_base(char *nbr, char *base_from, char *base_to)
{
	int	value;

	if (!base_is_valid(base_from) || !base_is_valid(base_to))
		return (NULL);
	value = ft_atoi_base(nbr, base_from);
	return (ft_itoa_base_int(value, base_to));
}
