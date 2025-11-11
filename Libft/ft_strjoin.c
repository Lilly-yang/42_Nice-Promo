/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 16:41:20 by lyang             #+#    #+#             */
/*   Updated: 2025/11/11 16:41:22 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static void	*ft_strcat_wo_end(char *dest, const char *src, int start)
{
	size_t	i;
	size_t	len;

	len = ft_strlen((char *)src);
	i = 0;
	while (i < len)
	{
		dest[start + i] = src[i];
		i++;
	}
	return (dest);
}

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*joined_str;
	size_t	len1;
	size_t	len2;

	if (!s1 || !s2)
		return (NULL);
	len1 = ft_strlen((char *)s1);
	len2 = ft_strlen((char *)s2);
	joined_str = (char *)malloc(sizeof(char) * (len1 + len2 + 1));
	if (!joined_str)
		return (NULL);
	ft_strcat_wo_end(joined_str, s1, 0);
	ft_strcat_wo_end(joined_str, s2, len1);
	joined_str[len1 + len2] = '\0';
	return (joined_str);
}
