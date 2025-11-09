/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/15 14:15:48 by lyang             #+#    #+#             */
/*   Updated: 2025/09/15 14:15:48 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
		i++;
	return (i);
}

char	*ft_strcat(char *dest, char *src)
{
	int	i;
	int	j;

	i = 0;
	j = 0;
	while (dest[i] != '\0')
		i++;
	while (src[j] != '\0')
	{
		dest[i] = src[j];
		i++;
		j++;
	}
	dest[i] = '\0';
	return (dest);
}

char	*if_size_0(void)
{
	char	*s;

	s = (char *)malloc(1);
	if (s)
		s[0] = '\0';
	return (s);
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	char	*s;
	int		i;
	int		len;

	if (size <= 0)
		return (if_size_0());
	i = 0;
	len = 0;
	while (i < size)
		len += ft_strlen(strs[i++]);
	len += ft_strlen(sep) * (size - 1);
	s = (char *)malloc(len + 1);
	if (!s)
		return (0);
	s[0] = '\0';
	i = 0;
	while (i < size)
	{
		ft_strcat(s, strs[i]);
		if (i < size - 1)
			ft_strcat(s, sep);
		i++;
	}
	return (s);
}
