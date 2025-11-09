/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_convert_base2.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yourlogin <you@42.fr>                      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/26 00:00:00 by yourlogin         #+#    #+#             */
/*   Updated: 2025/09/26 00:00:00 by yourlogin        ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

static int	ft_strlen(char *s)
{
	int i = 0;
	while (s && s[i])
		i++;
	return (i);
}

static int	base_is_valid(char *base)
{
	int i, j;

	if (!base || ft_strlen(base) < 2)
		return (0);
	i = 0;
	while (base[i])
	{
		if (base[i] == '+' || base[i] == '-' ||
			base[i] == ' ' || (base[i] >= 9 && base[i] <= 13))
			return (0);
		j = i + 1;
		while (base[j])
			if (base[i] == base[j++])
				return (0);
		i++;
	}
	return (1);
}

static int	count_digits_long(long n, int base_len)
{
	int count;

	if (n == 0)
		return (1);
	count = 0;
	while (n > 0)
	{
		n /= base_len;
		count++;
	}
	return (count);
}

char	*ft_itoa_base_int(int nbr, char *base)
{
	char	*res;
	int		b;
	long	n;        /* use long to safely handle INT_MIN */
	int		neg;
	int		len;
	int		i;

	if (!base_is_valid(base))
		return (NULL);
	b = ft_strlen(base);
	n = (long)nbr;
	neg = (n < 0);
	if (neg)
		n = -n;
	len = count_digits_long(n, b) + (neg ? 1 : 0);
	res = (char *)malloc((len + 1) * sizeof(char));
	if (!res)
		return (NULL);
	res[len] = '\0';
	if (n == 0)
		res[--len] = base[0];
	while (n > 0)
	{
		res[--len] = base[n % b];
		n /= b;
	}
	if (neg)
		res[0] = '-';
	return (res);
}
