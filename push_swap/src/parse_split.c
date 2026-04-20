#include "../include/push_swap.h"

static int	is_space(char c)
{
	return (c == ' ' || c == '\t' || c == '\n' || c == '\v' || c == '\f'
		|| c == '\r');
}

static int	count_words(const char *s)
{
	int	count;
	int	in_word;

	count = 0;
	in_word = 0;
	while (*s)
	{
		if (is_space(*s))
			in_word = 0;
		else if (!in_word)
		{
			in_word = 1;
			count++;
		}
		s++;
	}
	return (count);
}

static char	*dup_word(const char *start, int len)
{
	char	*word;
	int		i;

	word = malloc((size_t)len + 1);
	if (!word)
		return (NULL);
	i = 0;
	while (i < len)
	{
		word[i] = start[i];
		i++;
	}
	word[i] = '\0';
	return (word);
}

char	**split_whitespaces(const char *s)
{
	char	**out;
	int		count;
	int		i;
	int		len;

	count = count_words(s);
	out = malloc(sizeof(char *) * (count + 1));
	if (!out)
		return (NULL);
	i = 0;
	while (*s)
	{
		while (*s && is_space(*s))
			s++;
		len = 0;
		while (s[len] && !is_space(s[len]))
			len++;
		if (len > 0)
		{
			out[i] = dup_word(s, len);
			if (!out[i])
			{
				out[i] = NULL;
				return (free_tokens(out), NULL);
			}
			i++;
			s += len;
		}
	}
	out[i] = NULL;
	return (out);
}

void	free_tokens(char **tokens)
{
	int	i;

	if (!tokens)
		return ;
	i = 0;
	while (tokens[i])
	{
		free(tokens[i]);
		i++;
	}
	free(tokens);
}
