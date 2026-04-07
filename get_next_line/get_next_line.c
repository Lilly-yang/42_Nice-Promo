/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/30 17:53:15 by lyang             #+#    #+#             */
/*   Updated: 2026/04/07 12:51:12 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*read_to_stash(int fd, char *stash)
{
    char	*buffer;
    char	*tmp;
    ssize_t	bytes_read;

    buffer = (char *)malloc((BUFFER_SIZE + 1) * sizeof(char));
    if (!buffer)
        return (NULL);
    bytes_read = 1;
    while (!gnl_strchr(stash, '\n') && bytes_read > 0)
    {
        bytes_read = read(fd, buffer, BUFFER_SIZE);
        if (bytes_read < 0)
            return (free(buffer), free(stash), NULL);
        buffer[bytes_read] = '\0';
        tmp = gnl_strjoin(stash, buffer);
        free(stash);
        stash = tmp;
        if (!stash)
            return (free(buffer), NULL);
    }
    free(buffer);
    return (stash);
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

static char	*clean_stash(char *stash)
{
    char	*new_stash;
    size_t	i;

    if (!stash)
        return (NULL);
    i = 0;
    while (stash[i] && stash[i] != '\n')
        i++;
    if (!stash[i])
        return (free(stash), NULL);
    new_stash = gnl_substr(stash, i + 1, gnl_strlen(stash) - i - 1);
    free(stash);
    if (new_stash && new_stash[0] == '\0')
        return (free(new_stash), NULL);
    return (new_stash);
}

char	*get_next_line(int fd)
{
    static char	*stash;
    char			*line;

    if (fd < 0 || BUFFER_SIZE <= 0 || read(fd, 0, 0) < 0)
        return (free(stash), stash = NULL, NULL);
    stash = read_to_stash(fd, stash);
    if (!stash)
        return (NULL);
    line = extract_line(stash);
    stash = clean_stash(stash);
    return (line);
}