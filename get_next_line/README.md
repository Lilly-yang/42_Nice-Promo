*This project has been created as part of the 42 curriculum by lyang.*

# get_next_line

## Description

The **get_next_line** project is a C function that reads one line at a time from a file descriptor. The goal is to reimplement a line reader with strict constraints while maintaining efficiency and robustness.

**Key objectives:**
- Implement line-by-line reading without relying on libft
- Handle various input scenarios (regular files, standard input, edge cases)
- Work without `lseek()` to maintain streaming capabilities
- Avoid global variables (except for the internal state mechanism if applicable)
- Support configurable `BUFFER_SIZE` for flexible memory management

This project demonstrates understanding of:
- File I/O operations (`read()`)
- Dynamic memory management
- String manipulation
- Efficient buffering strategies

## Instructions

### Compilation

To use `get_next_line` in your project, include the header and compile together with your code:

```bash
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c your_file.c -o your_program
```

Or create a simple test program to verify functionality:

```bash
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c -c
ar rcs libgnl.a get_next_line.o get_next_line_utils.o
# Then link libgnl.a with your program
```

**Note:** You can adjust `BUFFER_SIZE` at compile time to test edge cases:
- Small buffer: `BUFFER_SIZE=1` (reads one byte at a time)
- Default: `BUFFER_SIZE=42`
- Large buffer: `BUFFER_SIZE=9999` or `BUFFER_SIZE=10000000`

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

**Static variable explanation:** A static `t_gnl_state` per file descriptor is used to preserve the stash between function calls. This is necessary because the function must return one line at a time while maintaining context for the next call. This is functionally equivalent to the file descriptor having built-in state (as real file I/O does).

### Justification

**Why this approach?**

1. **Efficiency**: By using buffering, we avoid excessive system calls. Reading in chunks of `BUFFER_SIZE` is much faster than reading one byte at a time.

2. **Robustness**: The algorithm gracefully handles:
   - Files without trailing newlines
   - Empty files
   - Very long lines
   - Multiple file descriptors simultaneously

3. **Flexibility**: `BUFFER_SIZE` is compile-time configurable, allowing optimization for different scenarios.

4. **Memory safety**: The stash grows dynamically only when needed, preventing both buffer overflows and excessive pre-allocation.

5. **Single read source**: The function maintains a single read position per file descriptor, necessary since `lseek()` is prohibited.

### Time Complexity

- **Per call**: O(n) where n is the length of the returned line
- **For entire file**: O(total bytes read), which is optimal since each byte must be read exactly once

### Space Complexity

- O(m) where m is the length of the longest line, due to the dynamic stash

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

### Tutorials & Articles

- Line-by-line file reading patterns
- File buffer management techniques
- State machine design in C

### AI Usage

AI tools (such as ChatGPT and Copilot) were used for:

- Understanding edge cases in line reading (e.g., files without trailing newlines)
- Debugging memory management issues related to dynamic allocation
- Explaining efficient buffer management strategies
- Code structure optimization feedback

All core algorithm design, implementation, and testing were completed manually and verified thoroughly with multiple test cases.

---

## Author

* lyang
