/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/19 11:32:09 by lyang             #+#    #+#             */
/*   Updated: 2025/11/19 11:53:35 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdarg.h>
#include <stdio.h>
#include "ft_printf.h"

int ft_printf(const char *format, ...)
{
	va_list args;
	int printed_chars;
	va_start(args, format);
	printed_chars = vdprintf(1, format, args);
	va_end(args);
	va_end(args);

	return (printed_chars);
}