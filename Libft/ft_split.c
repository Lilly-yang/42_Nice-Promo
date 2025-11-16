/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 16:40:34 by lyang             #+#    #+#             */
/*   Updated: 2025/11/11 16:40:37 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	count_words(const char *str, char delim)
{
	int	words;
	int	i;

	words = 0;
	i = 0;
	while (str[i])
	{
		while (str[i] && str[i] == delim)
			i++;
		if (str[i] && str[i] != delim)
		{
			words++;
			while (str[i] && str[i] != delim)
				i++;
		}
	}
	return (words);
}

static char	*ft_cpystr(const char *str, int start, int end)
{
	int		i;
	char	*dest;

	dest = (char *)malloc((end - start + 1) * sizeof(char));
	if (!dest)
		return (NULL);
	i = 0;
	while (start < end)
		dest[i++] = str[start++];
	dest[i] = '\0';
	return (dest);
}

static void	free_array(char **arr, int filled)
{
	int		i;

	i = 0;
	while (i < filled)
	{
		free(arr[i]);
		i++;
	}
	free(arr);
}

static char	*extract_word(char const *s, char c, int *i)
{
	int		start;
	char	*word;

	while (s[*i] && s[*i] == c)
		(*i)++;
	start = *i;
	while (s[*i] && s[*i] != c)
		(*i)++;
	word = ft_cpystr(s, start, *i);
	return (word);
}

char	**ft_split(char const *s, char c)
{
	char	**array;
	int		i;
	int		element_count;
	int		array_i;

	if (!s)
		return (NULL);
	element_count = count_words(s, c);
	array = (char **)malloc(sizeof(char *) * (element_count + 1));
	if (!array)
		return (NULL);
	i = 0;
	array_i = 0;
	while (array_i < element_count)
	{
		array[array_i] = extract_word(s, c, &i);
		if (!array[array_i++])
		{
			free_array(array, array_i - 1);
			return (NULL);
		}
	}
	array[array_i] = NULL;
	return (array);
}
