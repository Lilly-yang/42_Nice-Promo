/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/19 11:35:36 by lyang             #+#    #+#             */
/*   Updated: 2025/11/23 18:00:14 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>
# include <stdint.h>

static int	putc_out(char c);
static int	putstr_out(const char *s);
static int	putnbr_out(long n);
static int	putunbr_out(unsigned long n);
static int	puthex_out(unsigned long n, int upper);
static int	putptr_out(void *p);
static int	handle_spec_extra(va_list *args, char spec);
static int	handle_spec(va_list *args, char spec);
static int	print_one_char(const char **p);
static int	handle_percent_at(const char **p, va_list *args);
static int	printf_loop(const char *format, va_list *args);
int			ft_printf(const char *format, ...);

#endif