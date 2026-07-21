/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bench_report.c                                     :+:      :+:    :+:   */
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

static int	bench_total(t_bench *bench)
{
	int	total;

	total = bench->sa + bench->sb + bench->ss + bench->pa + bench->pb;
	total += bench->ra + bench->rb + bench->rr + bench->rra;
	total += bench->rrb + bench->rrr;
	return (total);
}

static void	print_strategy(t_mode used)
{
	if (used == MODE_SIMPLE)
		write_str("strategy: simple O(n^2)\n");
	else if (used == MODE_MEDIUM)
		write_str("strategy: medium O(n*sqrt(n))\n");
	else
		write_str("strategy: complex O(n log n)\n");
}

void	bench_print(double disorder, t_mode used, t_bench *bench)
{
	int	pct;

	pct = (int)(disorder * 10000.0 + 0.5);
	write_str("disorder: ");
	write_num(pct / 100);
	write_str(".");
	if ((pct % 100) < 10)
		write_str("0");
	write_num(pct % 100);
	write_str("%\n");
	print_strategy(used);
	write_str("total: ");
	write_num(bench_total(bench));
	write_str("\n");
	bench_print_counts(bench);
}
