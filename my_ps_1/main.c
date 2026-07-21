/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ylecain <ylecain@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:16 by lyang             #+#    #+#             */
/*   Updated: 2026/07/15 00:00:00 by ylecain          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static t_bench	*get_bench_ptr(t_config *cfg, t_bench *bench)
{
	if (!cfg->bench)
		return (NULL);
	bench_init(bench);
	return (bench);
}

static void	init_stacks(t_stack *a, t_stack *b, t_parse_result *parsed,
	t_bench *bench)
{
	stack_init(a, parsed->values, parsed->count, bench);
	stack_init(b, malloc(sizeof(int) * parsed->count), 0, bench);
	if (!b->arr)
		error_exit(a, NULL);
}

static t_mode	run_program(t_program *prog)
{
	t_bench		*bench_ptr;
	t_mode		used;
	double		disorder;

	bench_ptr = get_bench_ptr(&prog->cfg, &prog->bench);
	init_stacks(&prog->a, &prog->b, &prog->parsed, bench_ptr);
	disorder = compute_disorder(&prog->a);
	used = run_sort(prog->cfg.mode, &prog->a, &prog->b, disorder);
	if (prog->cfg.bench)
		bench_print(disorder, used, &prog->bench);
	stack_free(&prog->a);
	stack_free(&prog->b);
	return (used);
}

int	main(int argc, char **argv)
{
	t_program	prog;

	if (argc < 2)
		return (0);
	if (!parse_config(&argc, &argv, &prog.cfg))
		parse_error_exit();
	if (argc < 2 || !parse_arguments(argc, argv, &prog.parsed))
		parse_error_exit();
	run_program(&prog);
	return (0);
}
