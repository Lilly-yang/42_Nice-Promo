/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lyang <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/09 18:47:25 by lyang             #+#    #+#             */
/*   Updated: 2025/11/09 18:47:28 by lyang            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *dest, int c, size_t n)
{
	unsigned char	*p;
	unsigned char	value;

	p = (unsigned char *)dest;
	value = (unsigned char)c;
	while (n--)
		*p++ = value;
	return (dest);
}
