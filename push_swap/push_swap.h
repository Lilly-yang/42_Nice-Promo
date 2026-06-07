/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:42 by lyang             #+#    #+#             */
/*   Updated: 2026/06/08 00:55:43 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <limits.h>
# include <stddef.h>
# include <stdlib.h>
# include <unistd.h>

typedef struct s_stack
{
	int	*arr;
	int	size;
}t_stack;

typedef struct s_parse_result
{
	int	*values;
	int	count;
}t_parse_result;

/* parse */
int		parse_arguments(int argc, char **argv, t_parse_result *out);
void	free_tokens(char **tokens);

/* stack */
void	stack_init(t_stack *stack, int *values, int size);
void	stack_free(t_stack *stack);
int		stack_is_sorted(const t_stack *stack);

/* operations */
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

/* sort */
void	sort_stack(t_stack *a, t_stack *b);
void	sort_small(t_stack *a, t_stack *b);
void	sort_chunk(t_stack *a, t_stack *b);
void	sort_radix(t_stack *a, t_stack *b);
int		compress_values(t_stack *a);
int		index_of_max(const t_stack *stack);

/* utils */
int		ft_strcmp(const char *s1, const char *s2);
size_t	ft_strlen(const char *s);
void	*ft_memmove(void *dst, const void *src, size_t len);
char	**split_whitespaces(const char *s);

/* error */
void	error_exit(t_stack *a, t_stack *b);
void	parse_error_exit(void);

#endif
