/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/30 17:53:15 by lyang             #+#    #+#             */
/*   Updated: 2026/04/07 15:42:02 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

typedef struct s_gnl_state
{
    char	*stash;
    size_t	len;
    size_t	cap;
}	t_gnl_state;

static t_gnl_state	*gnl_state(void)
{
    static t_gnl_state	state;

    return (&state);
}

static int	stash_reserve(t_gnl_state *state, size_t needed)
{
    char	*new_stash;
    size_t	new_cap;
    size_t	i;

    if (needed <= state->cap)
        return (1);
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

static int	stash_append(t_gnl_state *state, const char *buffer, size_t bytes)
{
    size_t	i;

    if (!stash_reserve(state, state->len + bytes + 1))
        return (0);
    i = 0;
    while (i < bytes)
    {
        state->stash[state->len + i] = buffer[i];
        i++;
    }
    state->len += bytes;
    state->stash[state->len] = '\0';
    return (1);
}

static void	stash_reset(t_gnl_state *state)
{
    free(state->stash);
    state->stash = NULL;
    state->len = 0;
    state->cap = 0;
}

static char	*read_to_stash(int fd, t_gnl_state *state)
{
    char		*buffer;
    ssize_t		bytes_read;
    int			found_newline;

    buffer = (char *)malloc((BUFFER_SIZE + 1) * sizeof(char));
    if (!buffer)
        return (stash_reset(state), NULL);
    bytes_read = 1;
    found_newline = 0;
    while (bytes_read > 0 && !found_newline)
    {
        bytes_read = read(fd, buffer, BUFFER_SIZE);
        if (bytes_read < 0)
            return (free(buffer), stash_reset(state), NULL);
        found_newline = 0;
        for (ssize_t i = 0; i < bytes_read; i++)
        {
            if (buffer[i] == '\n')
            {
                found_newline = 1;
                break ;
            }
        }
        buffer[bytes_read] = '\0';
        if (!stash_append(state, buffer, (size_t)bytes_read))
            return (free(buffer), stash_reset(state), NULL);
    }
    free(buffer);
    return (state->stash);
}

static char	*extract_line(char *stash)
{
    size_t	i;

    if (!stash || !stash[0])
        return (NULL);
    i = 0;
    while (stash[i] && stash[i] != '\n')
        i++;
    if (stash[i] == '\n')
        return (gnl_substr(stash, 0, i + 1));
    return (gnl_substr(stash, 0, i));
}

static char	*clean_stash(t_gnl_state *state)
{
    char	*new_stash;
    size_t	i;
    size_t	remaining;

    if (!state->stash)
        return (NULL);
    i = 0;
    while (state->stash[i] && state->stash[i] != '\n')
        i++;
    if (!state->stash[i])
        return (stash_reset(state), NULL);
    remaining = state->len - i - 1;
    new_stash = gnl_substr(state->stash, i + 1, remaining);
    if (!new_stash)
    {
        stash_reset(state);
        return (NULL);
    }
    if (new_stash[0] == '\0')
    {
        free(state->stash);
        state->stash = NULL;
        state->len = 0;
        state->cap = 0;
        return (free(new_stash), NULL);
    }
    free(state->stash);
    state->stash = new_stash;
    state->len = remaining;
    state->cap = remaining + 1;
    return (new_stash);
}

char	*get_next_line(int fd)
{
    t_gnl_state	*state;
    char			*line;

    state = gnl_state();
    if (fd < 0 || BUFFER_SIZE <= 0 || read(fd, 0, 0) < 0)
        return (stash_reset(state), NULL);
    if (!read_to_stash(fd, state))
        return (NULL);
    line = extract_line(state->stash);
    if (!line)
        return (stash_reset(state), NULL);
    state->stash = clean_stash(state);
    return (line);
}