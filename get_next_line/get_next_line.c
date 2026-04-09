/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/30 17:53:15 by lyang             #+#    #+#             */
/*   Updated: 2026/04/09 13:25:55 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static t_gnl_state	*gnl_state(void)
{
	static t_gnl_state	state;

	return (&state);
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
		buffer[bytes_read] = '\0';
		if (!gnl_stash_append(state, buffer, (size_t)bytes_read))
			return (free(buffer), stash_reset(state), NULL);
		if (gnl_strchr(buffer, '\n'))
			found_newline = 1;
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

char	*get_next_line(int fd)
{
	t_gnl_state	*state;
	char		*line;

	state = gnl_state();
	if (fd < 0 || BUFFER_SIZE <= 0 || read(fd, 0, 0) < 0)
		return (stash_reset(state), NULL);
	if (!read_to_stash(fd, state))
		return (NULL);
	line = extract_line(state->stash);
	if (!line)
		return (stash_reset(state), NULL);
	state->stash = gnl_clean_stash(state);
	return (line);
}
