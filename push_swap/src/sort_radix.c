#include "../include/push_swap.h"

static void	copy_arr(int *dst, const int *src, int n)
{
	int	i;

	i = 0;
	while (i < n)
	{
		dst[i] = src[i];
		i++;
	}
}

static void	sort_ints(int *arr, int n)
{
	int	i;
	int	j;
	int	tmp;

	i = 0;
	while (i < n - 1)
	{
		j = 0;
		while (j < n - 1 - i)
		{
			if (arr[j] > arr[j + 1])
			{
				tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
			j++;
		}
		i++;
	}
}

static int	find_index(const int *arr, int n, int value)
{
	int	i;

	i = 0;
	while (i < n)
	{
		if (arr[i] == value)
			return (i);
		i++;
	}
	return (-1);
}

static int	compress_values(t_stack *a)
{
	int	*sorted;
	int	i;
	int	idx;

	sorted = malloc(sizeof(int) * a->size);
	if (!sorted)
		return (0);
	copy_arr(sorted, a->arr, a->size);
	sort_ints(sorted, a->size);
	i = 0;
	while (i < a->size)
	{
		idx = find_index(sorted, a->size, a->arr[i]);
		if (idx < 0)
			return (free(sorted), 0);
		a->arr[i] = idx;
		i++;
	}
	free(sorted);
	return (1);
}

void	sort_radix(t_stack *a, t_stack *b)
{
	int	max_bits;
	int	bit;
	int	i;
	int	n;

	if (!compress_values(a))
		error_exit(a, b);
	n = a->size;
	max_bits = 0;
	while (((n - 1) >> max_bits) != 0)
		max_bits++;
	bit = 0;
	while (bit < max_bits)
	{
		i = 0;
		while (i < n)
		{
			if (((a->arr[0] >> bit) & 1) == 0)
				op_pb(a, b, 1);
			else
				op_ra(a, 1);
			i++;
		}
		while (b->size > 0)
			op_pa(a, b, 1);
		bit++;
	}
}
