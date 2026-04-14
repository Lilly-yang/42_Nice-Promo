#include "get_next_line.h"

#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

static int	assert_line(char *got, const char *expected, int index)
{
	if (!got && !expected)
		return (1);
	if (!got || !expected)
	{
		printf("[FAIL] line %d: got %s, expected %s\n",
			index,
			got ? got : "NULL",
			expected ? expected : "NULL");
		free(got);
		return (0);
	}
	if (strcmp(got, expected) != 0)
	{
		printf("[FAIL] line %d: got \"%s\", expected \"%s\"\n",
			index, got, expected);
		free(got);
		return (0);
	}
	printf("[OK]   line %d: \"%s\"\n", index, got);
	free(got);
	return (1);
}

int	main(void)
{
	const char	*file_name = "tmp_custom_sep.txt";
	const char	*content = "first!second!!fourth!last";
	const char	*expected[] = {"first!", "second!", "!", "fourth!", "last", NULL};
	int			fd;
	int			i;
	char		*line;

	fd = open(file_name, O_CREAT | O_TRUNC | O_WRONLY, 0644);
	if (fd < 0)
		return (perror("open write"), 1);
	if (write(fd, content, strlen(content)) < 0)
		return (close(fd), perror("write"), 1);
	if (close(fd) < 0)
		return (perror("close write"), 1);
	fd = open(file_name, O_RDONLY);
	if (fd < 0)
		return (perror("open read"), 1);
	i = 0;
	while (expected[i])
	{
		line = get_next_line(fd);
		if (!assert_line(line, expected[i], i + 1))
			return (close(fd), unlink(file_name), 1);
		i++;
	}
	line = get_next_line(fd);
	if (!assert_line(line, NULL, i + 1))
		return (close(fd), unlink(file_name), 1);
	if (close(fd) < 0)
		return (unlink(file_name), perror("close read"), 1);
	if (unlink(file_name) < 0)
		return (perror("unlink"), 1);
	printf("\nAll custom separator tests passed.\n");
	return (0);
}