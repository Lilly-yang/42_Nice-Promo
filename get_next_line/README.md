*This project has been created as part of the 42 curriculum by lyang.*

# get_next_line

## Description

The **get_next_line** project is a C function that reads one line at a time from a file descriptor. The goal is to reimplement a line reader with strict constraints while maintaining efficiency and robustness.

## Instructions

### Compilation

To use `get_next_line` in your project, include the header and compile together with your code:

```bash
cc -Wall -Wextra -Werror get_next_line.c get_next_line_utils.c your_code.c
```

**Note:** You can adjust `BUFFER_SIZE` at compile time to test edge cases:

```bash
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c your_code.c
```


### Usage

Include the header in your C code:

```c
#include "get_next_line.h"

int main(void)
{
    int fd = open("file.txt", O_RDONLY);
    char *line;
    
    while ((line = get_next_line(fd)) != NULL)
    {
        printf("%s", line);
        free(line);
    }
    close(fd);
    return (0);
}
```

The function returns:
- A pointer to the next line (allocated, must be freed)
- `NULL` when EOF is reached or on error

## Algorithm

### Overview

The selected algorithm uses a **persistent stash** with **amortized dynamic growth** to efficiently handle variable-length lines while maintaining a single pass through the file.

### Strategy

1. **Maintain a stash**: A dynamic buffer that preserves unprocessed characters between function calls
2. **Read chunks**: Use `read()` to fetch `BUFFER_SIZE` bytes at a time
3. **Append to stash**: Accumulate data from multiple reads until a newline is found or EOF is reached
4. **Extract line**: When a newline is encountered, extract the line from the stash
5. **Preserve remainder**: Keep remaining characters in the stash for the next call

### Data Structures

The implementation uses a state structure to maintain continuity across calls:

```c
typedef struct s_gnl_state
{
    char    *stash;   // Dynamic buffer holding unprocessed data
    size_t  len;      // Current length of data in stash
    size_t  cap;      // Allocated capacity of the stash
}   t_gnl_state;
```

### Justification

1. **Efficiency**: Reading in chunks avoids excessive system calls and is faster than byte-by-byte reading.

2. **Flexibility**: `BUFFER_SIZE` is compile-time configurable, allowing optimization for different scenarios.

3. **Memory safety**: The stash grows dynamically only when needed, preventing inefficient allocation.

4. **Single read source**: The function maintains a single read position per file descriptor, necessary since `lseek()` is prohibited.

## Resources

### Official Documentation

- [POSIX read() function](https://pubs.opengroup.org/onlinepubs/9699919799/functions/read.html)
- [C dynamic memory allocation](https://en.cppreference.com/w/c/memory)
- Linux manual pages:
  ```bash
  man 2 read
  man malloc
  man free
  ```

### AI Usage

AI tools (such as ChatGPT and Copilot) were used for:

- Understanding edge cases in line reading (e.g., files without trailing newlines)
- Debugging memory management issues related to dynamic allocation
- Explaining efficient buffer management strategies
- Code structure optimization feedback
