/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/30 17:53:07 by lyang             #+#    #+#             */
/*   Updated: 2026/04/09 13:25:55 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# include <unistd.h>
# include <stdlib.h>

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 42
# endif

typedef struct s_gnl_state
{
	char	*stash;
	size_t	len;
	size_t	cap;
}	t_gnl_state;

char	*get_next_line(int fd);
char	*gnl_strchr(const char *s, int c);
char	*gnl_substr(char const *s, unsigned int start, size_t len);
int		gnl_stash_append(t_gnl_state *state, const char *buffer, size_t bytes);
char	*gnl_clean_stash(t_gnl_state *state);

#endif