/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_out.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/23 17:23:48 by lyang             #+#    #+#             */
/*   Updated: 2026/04/07 11:05:39 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	putc_out(char c)
{
	if (write(1, &c, 1) != 1)
		return (-1);
	return (1);
}

int	putstr_out(const char *s)
{
	size_t	len;

	if (!s)
		s = "(null)";
	len = 0;
	while (s[len])
		len++;
	if (len && write(1, s, len) != (ssize_t)len)
		return (-1);
	return ((int)len);
}

int	putptr_out(void *p)
{
	unsigned long	addr;
	int				cnt;

	if (!p)
		return (putstr_out("(nil)"));
	if (write(1, "0x", 2) != 2)
		return (-1);
	addr = (unsigned long)(uintptr_t)p;
	cnt = 2;
	cnt += puthex_out(addr, 0);
	return (cnt);
}
