#include <stdio.h>
#include "ft_printf.h"

int main(void)
{
    // 基础测试
    printf("OG: %c %s %p %d %i %u %x %X %%\n",
        'A', "hello", &main, 42, -42, 42, 42, 42);
    ft_printf("FT: %c %s %p %d %i %u %x %X %%\n",
        'A', "hello", &main, 42, -42, 42, 42, 42);

    return (0);
}