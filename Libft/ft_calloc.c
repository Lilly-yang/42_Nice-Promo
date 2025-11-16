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
	size_t			n;

	if (size != 0 && nmemb > ((size_t)-1) / size)
		return (NULL);
	n = nmemb * size;
	p = malloc(n);
	if (!p)
		return (NULL);
	ft_bzero(p, n);
	return (p);
}
