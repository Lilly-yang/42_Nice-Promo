/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_sub.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/23 17:59:14 by lyang             #+#    #+#             */
/*   Updated: 2025/11/23 17:59:21 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	handle_spec_extra(va_list *args, char spec)
{
	if (spec == 'u')
		return (putunbr_out((unsigned long)va_arg(*args, unsigned int)));
	if (spec == 'x')
		return (puthex_out((unsigned long)va_arg(*args, unsigned int), 0));
	if (spec == 'X')
		return (puthex_out((unsigned long)va_arg(*args, unsigned int), 1));
	if (spec == 'p')
		return (putptr_out(va_arg(*args, void *)));
	if (putc_out('%') < 0 || putc_out(spec) < 0)
		return (-1);
	return (2);
}

static int	handle_spec(va_list *args, char spec)
{
	if (spec == '%')
	{
		if (putc_out('%') < 0)
			return (-1);
		return (1);
	}
	if (spec == 'c')
	{
		if (putc_out((char)va_arg(*args, int)) < 0)
			return (-1);
		return (1);
	}
	if (spec == 's')
		return (putstr_out(va_arg(*args, char *)));
	if (spec == 'd' || spec == 'i')
		return (putnbr_out((long)va_arg(*args, int)));
	return (handle_spec_extra(args, spec));
}

static int	print_one_char(const char **p)
{
	if (putc_out(**p) < 0)
		return (-1);
	(*p)++;
	return (1);
}

static int	handle_percent_at(const char **p, va_list *args)
{
	int	tmp;

	(*p)++;
	if (**p == '\0')
		return (0);
	tmp = handle_spec(args, **p);
	if (tmp < 0)
		return (-1);
	(*p)++;
	return (tmp);
}

static int	printf_loop(const char *format, va_list *args)
{
	const char	*p;
	int			total;
	int			tmp;

	total = 0;
	p = format;
	while (*p)
	{
		if (*p != '%')
		{
			tmp = print_one_char(&p);
			if (tmp < 0)
				return (-1);
			total += tmp;
			continue ;
		}
		tmp = handle_percent_at(&p, args);
		if (tmp == 0)
			break ;
		if (tmp < 0)
			return (-1);
		total += tmp;
	}
	return (total);
}
