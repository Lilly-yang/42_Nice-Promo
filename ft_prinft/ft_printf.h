/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/19 11:35:36 by lyang             #+#    #+#             */
/*   Updated: 2026/04/06 11:49:30 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>
# include <stdint.h>

int			putc_out(char c);
int			putstr_out(const char *s);
int			putnbr_out(long n);
int			putunbr_out(unsigned long n);
int			puthex_out(unsigned long n, int upper);
int			putptr_out(void *p);
int			handle_spec(va_list *args, char spec);
int			print_one_char(const char **p);
int			handle_percent_at(const char **p, va_list *args);
int			printf_loop(const char *format, va_list *args);
int			ft_printf(const char *format, ...);

#endif