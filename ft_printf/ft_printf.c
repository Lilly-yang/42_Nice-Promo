/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/19 11:32:09 by lyang             #+#    #+#             */
/*   Updated: 2026/04/06 11:48:23 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		total;

	if (!format)
		return (0);
	va_start(args, format);
	total = printf_loop(format, &args);
	va_end(args);
	return (total);
}
