/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/16 11:59:49 by lyang             #+#    #+#             */
/*   Updated: 2025/09/16 11:59:50 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	if_in(char *str, char c)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] == c)
			return (1);
		i++;
	}
	return (0);
}

int	count_words(char *str, char *charset)
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

void	*ft_cpystr(char *str, int start, int end)
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

char	**ft_split(char *str, char *charset)
{
	char	**array;
	int		i;
	int		element_count;
	int		array_i;
	int		start;

	array = (char **)malloc(sizeof(char *) * (count_words(str, charset) + 1));
	if (!array)
		return (NULL);
	i = 0;
	element_count = 0;
	array_i = 0;
	while (str[i] != '\0')
	{
		while (str[i] && if_in(charset, str[i]))
			i++;
		start = i;
		while (str[i] && !if_in(charset, str[i]))
			i++;
		if (start < i)
			array[array_i++] = ft_cpystr(str, start, i);
	}
	array[array_i] = NULL;
	return (array);
}
