/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_mode.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/09 00:00:00 by ylecain           #+#    #+#             */
/*   Updated: 2026/07/22 16:12:47 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	apply_flag(const char *flag, t_config *cfg)
{
	if (!ft_strcmp(flag, "--simple"))
		cfg->mode = MODE_SIMPLE;
	else if (!ft_strcmp(flag, "--medium"))
		cfg->mode = MODE_MEDIUM;
	else if (!ft_strcmp(flag, "--complex"))
		cfg->mode = MODE_COMPLEX;
	else if (!ft_strcmp(flag, "--adaptive"))
		cfg->mode = MODE_ADAPTIVE;
	else if (!ft_strcmp(flag, "--bench"))
		cfg->bench = 1;
	else if (!ft_strcmp(flag, "--count-only"))
	{
		cfg->bench = 1;
		cfg->count_only = 1;
	}
	else
		return (0);
	return (1);
}

int	parse_config(int *argc, char ***argv, t_config *cfg)
{
	cfg->mode = MODE_ADAPTIVE;
	cfg->bench = 0;
	cfg->count_only = 0;
	while (*argc > 1 && (*argv)[1][0] == '-' && (*argv)[1][1] == '-')
	{
		if (!apply_flag((*argv)[1], cfg))
			return (0);
		(*argv)++;
		(*argc)--;
	}
	return (1);
}
