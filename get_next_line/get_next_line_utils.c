/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/30 17:53:23 by lyang             #+#    #+#             */
/*   Updated: 2026/04/09 13:25:55 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*gnl_strchr(const char *s, int c)
{
	if (!s)
		return (NULL);
	while (*s)
	{
		if (*s == (char)c)
			return ((char *)s);
		s++;
	}
	if ((char)c == '\0')
		return ((char *)s);
	return (NULL);
}

static int	gnl_stash_resize(t_gnl_state *state, size_t needed)
{
	char	*new_stash;
	size_t	new_cap;
	size_t	i;

	new_cap = state->cap;
	if (new_cap == 0)
		new_cap = 1;
	while (new_cap < needed)
		new_cap *= 2;
	new_stash = (char *)malloc(new_cap * sizeof(char));
	if (!new_stash)
		return (0);
	i = 0;
	while (i < state->len)
	{
		new_stash[i] = state->stash[i];
		i++;
	}
	free(state->stash);
	state->stash = new_stash;
	state->cap = new_cap;
	return (1);
}

int	gnl_stash_append(t_gnl_state *state, const char *buffer, size_t bytes)
{
	size_t	i;

	if (state->len + bytes + 1 > state->cap)
		if (!gnl_stash_resize(state, state->len + bytes + 1))
			return (0);
	i = 0;
	while (i < bytes)
	{
		state->stash[state->len + i] = buffer[i];
		i++;
	}
	state->len += bytes;
	return (state->stash[state->len] = '\0', 1);
}

char	*gnl_substr(char const *s, unsigned int start, size_t len)
{
	char	*sub;
	size_t	i;
	size_t	s_len;

	if (!s)
		return (NULL);
	s_len = 0;
	while (s[s_len])
		s_len++;
	if (start >= s_len)
		len = 0;
	else if (len > s_len - start)
		len = s_len - start;
	sub = (char *)malloc((len + 1) * sizeof(char));
	if (!sub)
		return (NULL);
	i = 0;
	while (i < len)
	{
		sub[i] = s[start + i];
		i++;
	}
	sub[i] = '\0';
	return (sub);
}

char	*gnl_clean_stash(t_gnl_state *state)
{
	char	*new_stash;
	size_t	i;
	size_t	remaining;

	if (!state->stash)
		return (NULL);
	i = 0;
	while (state->stash[i] && state->stash[i] != '\n')
		i++;
	if (!state->stash[i] || state->len - i - 1 == 0)
		return (free(state->stash), state->stash = NULL, state->len = 0,
			state->cap = 0, NULL);
	remaining = state->len - i - 1;
	new_stash = gnl_substr(state->stash, i + 1, remaining);
	if (!new_stash)
		return (free(state->stash), state->stash = NULL, state->len = 0,
			state->cap = 0, NULL);
	free(state->stash);
	state->stash = new_stash;
	state->len = remaining;
	state->cap = remaining + 1;
	return (new_stash);
}
