#include <stdio.h>
#include <limits.h>
#include "ft_printf.h"

int main(void)
{
	int a;
	int b;

	a = printf("OG1: s=%s p=%p d=%d i=%i u=%u x=%x X=%X %%\n",
		(char *)NULL, (void *)NULL, INT_MIN, INT_MAX, 0U, 0U, 0U);
	b = ft_printf("FT1: s=%s p=%p d=%d i=%i u=%u x=%x X=%X %%\n",
		(char *)NULL, (void *)NULL, INT_MIN, INT_MAX, 0U, 0U, 0U);
	printf("RET1 og=%d ft=%d\n", a, b);

	b = ft_printf("FT2: bad=%q end\n", 123);
	printf("RET2 ft=%d (unknown spec test)\n", b);

	a = printf("OG3: %% %% %%\n");
	b = ft_printf("FT3: %% %% %%\n");
	printf("RET3 og=%d ft=%d\n", a, b);
	return (0);
}
