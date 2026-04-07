*This project has been created as part of the 42 curriculum by lyang.*

# ft_printf

## Description

The **ft_printf** project consists of reimplementing a simplified version of the standard C function `printf`. The goal is to understand how formatted output works internally by handling variable arguments and parsing format specifiers.

This project focuses on low-level programming concepts such as:

* Variadic functions
* String parsing
* Memory management
* Number conversion

The implemented function reproduces the behavior of `printf` for a subset of format specifiers.

---

## Instructions

### Compilation

Clone the repository and compile using `make`:

```bash
git clone <your_repo_url>
cd ft_printf
make
```

This will generate the static library:

```bash
libftprintf.a
```

---

### Usage

Include the header in your C file:

```c
#include "ft_printf.h"
```

Then compile your program with:

```bash
gcc main.c -L. -lftprintf
```

---

### Supported Format Specifiers

| Specifier   | Description             |
| ----------- | ----------------------- |
| `%c`        | Character               |
| `%s`        | String                  |
| `%p`        | Pointer address         |
| `%d` / `%i` | Integer                 |
| `%u`        | Unsigned integer        |
| `%x`        | Hexadecimal (lowercase) |
| `%X`        | Hexadecimal (uppercase) |
| `%%`        | Percent sign            |

---

<!-- ## Algorithm & Data Structures

### Parsing Strategy

The main algorithm consists of iterating through the format string character by character:

1. Print regular characters directly.
2. When encountering `%`, switch to parsing mode.
3. Identify the format specifier.
4. Retrieve the corresponding argument using `va_arg`.
5. Convert and print the value.

---

### Variadic Arguments Handling

The project uses the `<stdarg.h>` library:

* `va_start` initializes argument traversal
* `va_arg` retrieves each argument
* `va_end` cleans up

---

### Number Conversion

Custom conversion functions are implemented:

* Integer → string (base 10)
* Unsigned integer → string
* Hexadecimal conversion (base 16)
* Pointer formatting (`0x` prefix)

These are typically implemented using:

* Recursion or iteration
* Division and modulo operations

---

### Data Structures

No complex data structures are required. The project mainly relies on:

* Basic types (`int`, `char`, `unsigned int`, `void *`)
* Strings (`char *`)
* Internal helper functions

---

## Features

* Reimplementation of `printf`
* Support for multiple format specifiers
* Modular and reusable code structure
* Accurate return value (number of printed characters)

--- -->

## Resources

### Documentation

* C standard library: `printf`
* `stdarg.h` documentation
* Linux manual:

  ```bash
  man 3 printf
  ```

---

### Tutorials & Articles

* Variadic functions in C
* Number base conversion
* Writing custom printf implementations

---

### AI Usage

AI tools (such as ChatGPT) were used for:

* Understanding variadic functions
* Clarifying edge cases and expected behavior
* Structuring the project and improving code organization

All implementation and debugging were done manually.

---

<!-- ## Notes

* This implementation does not cover all features of the original `printf`.
* Behavior may differ in edge cases not required by the subject.
* The project prioritizes clarity and correctness over full compliance with the libc version.

--- -->

## 👤 Author

* liyang

---
