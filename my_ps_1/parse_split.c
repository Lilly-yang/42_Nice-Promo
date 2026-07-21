/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_split.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <lyang@student.42nice.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 00:55:35 by lyang             #+#    #+#             */
/*   Updated: 2026/07/09 00:00:00 by ylecain          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	free_words(char **out, int count)
{
	while (count > 0)
	{
		count--;
		free(out[count]);
	}
	free(out);
}

static int	count_words(const char *s)
{
	int	count;
	int	in_word;

	count = 0;
	in_word = 0;
	while (*s)
	{
		if (is_space(*s))
			in_word = 0;
		else if (!in_word)
		{
			in_word = 1;
			count++;
		}
		s++;
	}
	return (count);
}

static char	*dup_word(const char *start, int len)
{
	char	*word;
	int		i;

	word = malloc((size_t)len + 1);
	if (!word)
		return (NULL);
	i = 0;
	while (i < len)
	{
		word[i] = start[i];
		i++;
	}
	word[i] = '\0';
	return (word);
}

static char	**fill_words(const char *s, char **out)
{
	int	word;
	int	len;

	word = 0;
	while (*s)
	{
		while (*s && is_space(*s))
			s++;
		len = 0;
		while (s[len] && !is_space(s[len]))
			len++;
		if (len > 0)
		{
			out[word] = dup_word(s, len);
			if (!out[word])
			{
				free_words(out, word);
				return (NULL);
			}
			word++;
			s += len;
		}
	}
	out[word] = NULL;
	return (out);
}

char	**split_whitespaces(const char *s)
{
	char	**out;
	int		count;

	count = count_words(s);
	out = malloc(sizeof(char *) * (count + 1));
	if (!out)
		return (NULL);
	if (!fill_words(s, out))
		return (NULL);
	return (out);
}
