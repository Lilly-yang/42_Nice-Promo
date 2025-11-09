/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/09 19:46:32 by lyang             #+#    #+#             */
/*   Updated: 2025/11/09 19:46:33 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	void			*p;
	unsigned char	*tmp;
	size_t			n;

	n = nmemb * size;
	p = malloc(n);
	if (p)
	{
		tmp = (unsigned char *)p;
		while (n--)
			*tmp++ = '0';
	}
	return (p);
}
