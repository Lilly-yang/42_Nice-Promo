/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bench_counts.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ylecain <ylecain@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/15 00:00:00 by ylecain           #+#    #+#             */
/*   Updated: 2026/07/15 00:00:00 by ylecain          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	write_str(const char *s)
{
	write(2, s, ft_strlen(s));
}

static void	write_num(int n)
{
	char	buf[12];
	int		idx;

	idx = 11;
	buf[idx--] = '\0';
	if (n == 0)
		write(2, "0", 1);
	while (n > 0)
	{
		buf[idx--] = (n % 10) + '0';
		n /= 10;
	}
	if (buf[idx + 1] != '\0')
		write(2, &buf[idx + 1], ft_strlen(&buf[idx + 1]));
}

static void	print_count(const char *name, int count)
{
	write_str(name);
	write_str(": ");
	write_num(count);
	write_str("\n");
}

void	bench_print_counts(t_bench *bench)
{
	print_count("sa", bench->sa);
	print_count("sb", bench->sb);
	print_count("ss", bench->ss);
	print_count("pa", bench->pa);
	print_count("pb", bench->pb);
	print_count("ra", bench->ra);
	print_count("rb", bench->rb);
	print_count("rr", bench->rr);
	print_count("rra", bench->rra);
	print_count("rrb", bench->rrb);
	print_count("rrr", bench->rrr);
}
