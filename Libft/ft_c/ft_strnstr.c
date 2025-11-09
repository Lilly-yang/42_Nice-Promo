/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/09 19:34:09 by lyang             #+#    #+#             */
/*   Updated: 2025/11/09 19:34:10 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	int	i;
	int	j;

	if (little[0] == '\0')
		return (big);
	i = 0;
	while (big[i] != '\0' && len--)
	{
		j = 0;
		while (big[i + j] != '\0' && big[i + j] == little[j])
		{
			j++;
			if (little[j] == '\0')
				return (&big[i]);
		}
		i++;
	}
	return (NULL);
}
