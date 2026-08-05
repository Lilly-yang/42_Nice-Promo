/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:42 by lyang             #+#    #+#             */
/*   Updated: 2026/07/22 16:17:26 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <limits.h>
# include <stddef.h>
# include <stdlib.h>
# include <unistd.h>

typedef enum e_mode
{
	MODE_SIMPLE,
	MODE_MEDIUM,
	MODE_COMPLEX,
	MODE_ADAPTIVE
}	t_mode;

typedef struct s_config
{
	t_mode	mode;
	int		bench;
	int		count_only;
}	t_config;

typedef struct s_bench
{
	int	sa;
	int	sb;
	int	ss;
	int	pa;
	int	pb;
	int	ra;
	int	rb;
	int	rr;
	int	rra;
	int	rrb;
	int	rrr;
	int count_only;
}	t_bench;

typedef struct s_stack
{
	int		*arr;
	int		size;
	t_bench	*bench;
}	t_stack;

typedef struct s_parse_result
{
	int	*values;
	int	count;
}	t_parse_result;

typedef struct s_program
{
	t_config		cfg;
	t_parse_result	parsed;
	t_stack			a;
	t_stack			b;
	t_bench			bench;
}	t_program;

int		parse_arguments(int argc, char **argv, t_parse_result *out);
int		parse_config(int *argc, char ***argv, t_config *cfg);
int		parse_int_strict(const char *s, int *out);
void	free_tokens(char **tokens);

void	stack_init(t_stack *stack, int *values, int size, t_bench *bench);
void	stack_free(t_stack *stack);
int		stack_is_sorted(const t_stack *stack);

void	op_sa(t_stack *a, int print);
void	op_sb(t_stack *b, int print);
void	op_ss(t_stack *a, t_stack *b, int print);
void	op_pa(t_stack *a, t_stack *b, int print);
void	op_pb(t_stack *a, t_stack *b, int print);
void	op_ra(t_stack *a, int print);
void	op_rb(t_stack *b, int print);
void	op_rr(t_stack *a, t_stack *b, int print);
void	op_rra(t_stack *a, int print);
void	op_rrb(t_stack *b, int print);
void	op_rrr(t_stack *a, t_stack *b, int print);

void	sort_small(t_stack *a, t_stack *b);
void	sort_chunk(t_stack *a, t_stack *b);
void	sort_radix(t_stack *a, t_stack *b);
t_mode	run_sort(t_mode mode, t_stack *a, t_stack *b, double disorder);
int		compress_values(t_stack *a);
int		index_of_max(const t_stack *stack);

int		ft_strcmp(const char *s1, const char *s2);
size_t	ft_strlen(const char *s);
void	*ft_memmove(void *dst, const void *src, size_t len);
char	**split_whitespaces(const char *s);
int		is_space(char c);
double	compute_disorder(t_stack *a);
void	bench_init(t_bench *bench);
void	bench_print(double disorder, t_mode used, t_bench *bench);
void	bench_print_counts(t_bench *bench);

void	error_exit(t_stack *a, t_stack *b);
void	parse_error_exit(void);

#endif
