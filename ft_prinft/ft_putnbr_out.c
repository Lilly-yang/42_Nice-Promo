/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_out.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/23 17:36:10 by lyang             #+#    #+#             */
/*   Updated: 2025/11/23 17:37:38 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	putnbr_out(long n)
{
	char	buf[32];
	int		i;
	int		neg;
	int		count;

	neg = (n < 0);
	if (neg)
		n = -n;
	i = 0;
	if (n == 0)
		buf[i++] = '0';
	while (n > 0)
	{
		buf[i++] = '0' + (n % 10);
		n /= 10;
	}
	if (neg)
		buf[i++] = '-';
	count = i;
	while (--i >= 0)
		if (write(1, &buf[i], 1) != 1)
			return (-1);
	return (count);
}

static int	putunbr_out(unsigned long n)
{
	char	buf[32];
	int		i;
	int		count;

	i = 0;
	if (n == 0)
		buf[i++] = '0';
	while (n > 0)
	{
		buf[i++] = '0' + (n % 10);
		n /= 10;
	}
	count = i;
	while (--i >= 0)
		if (write(1, &buf[i], 1) != 1)
			return (-1);
	return (count);
}

static int	puthex_out(unsigned long n, int upper)
{
	char		buf[32];
	const char	*digits;
	int			i;
	int			count;

	if (upper)
		digits = "0123456789ABCDEF";
	else
		digits = "0123456789abcdef";
	i = 0;
	if (n == 0)
		buf[i++] = '0';
	while (n > 0)
	{
		buf[i++] = digits[n % 16];
		n /= 16;
	}
	count = i;
	while (--i >= 0)
		if (write(1, &buf[i], 1) != 1)
			return (-1);
	return (count);
}
