/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_out.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/23 17:23:48 by lyang             #+#    #+#             */
/*   Updated: 2025/11/23 17:36:33 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	putc_out(char c)
{
	if (write(1, &c, 1) != 1)
		return (-1);
	return (1);
}

static int	putstr_out(const char *s)
{
	size_t	len;

	if (!s)
		s = "(null)";
	len = strlen(s);
	if (len && write(1, s, len) != (ssize_t)len)
		return (-1);
	return ((int)len);
}

static int	putptr_out(void *p)
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
