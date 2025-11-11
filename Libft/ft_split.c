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

static int	if_in(char *charset, char c)
{
	int	i;

	i = 0;
	while (charset[i] != '\0')
	{
		if (charset[i] == c)
			return (1);
		i++;
	}
	return (0);
}

static int	count_words(char *str, char *charset)
{
	int	words;
	int	i;

	words = 0;
	i = 0;
	while (str[i] != '\0')
	{
		while (str[i] && if_in(charset, str[i]))
			i++;
		if (str[i] && !if_in(charset, str[i]))
		{
			words++;
			while (str[i] && !if_in(charset, str[i]))
				i++;
		}
	}
	return (words);
}

static char	*ft_cpystr(char *str, int start, int end)
{
	int		i;
	char	*dest;

	dest = malloc(end - start + 1);
	if (!dest)
		return (NULL);
	i = 0;
	while (start < end)
	{
		dest[i++] = str[start++];
	}
	dest[i] = '\0';
	return (dest);
}

char	**ft_split(char const *s, char c)
{
	char	**array;
	int		i;
	int		element_count;
	int		array_i;
	int		start;

	if (!s)
		return (NULL);
	element_count = count_words((char *)s, (char *)&c);
	array = (char **)malloc(sizeof(char *) * (element_count + 1));
	if (!array)
		return (NULL);
	i = 0;
	array_i = 0;
	while (array_i < element_count)
	{
		while (s[i] && s[i] == c)
			i++;
		start = i;
		while (s[i] && s[i] != c)
			i++;
		array[array_i++] = ft_cpystr((char *)s, start, i);
	}
	array[array_i] = NULL;
	return (array);
}
