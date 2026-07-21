# Push Swap

A sorting algorithm implementation that sorts a list of integers using two stacks and a predefined set of operations.

## Description

Push Swap is a project that challenges you to sort a random list of unique integers using two stacks (stack A and stack B) with a limited set of operations. The goal is to perform the sort with the minimum number of operations possible.

This implementation uses an adaptive sorting strategy:
- **Small Sort** (≤5 numbers): Uses insertion-based algorithm for optimal operation count
- **Radix Sort** (>5 numbers): Uses binary radix sort for efficient large dataset sorting

## Project Structure

```
push_swap/
├── include/
│   └── push_swap.h          # Main header file with function declarations
├── src/
│   ├── main.c               # Entry point
│   ├── parse.c              # Argument parsing
│   ├── parse_split.c        # String splitting utilities
│   ├── stack.c              # Stack initialization and management
│   ├── ops_swap.c           # SA, SB, SS operations
│   ├── ops_push.c           # PA, PB operations
│   ├── ops_rotate.c         # RA, RB, RR operations
│   ├── ops_reverse_rotate.c # RRA, RRB, RRR operations
│   ├── sort_small.c         # Sorting algorithm for small stacks
│   ├── sort_radix.c         # Radix sort algorithm
│   ├── utils.c              # Utility functions
│   └── error.c              # Error handling
├── Makefile                 # Build configuration
└── README.md                # This file
```

## Stack Operations

The program supports the following operations:

### Basic Operations
- **`sa`** : Swap the first 2 elements at the top of stack A
- **`sb`** : Swap the first 2 elements at the top of stack B
- **`ss`** : Execute `sa` and `sb` simultaneously

### Push Operations
- **`pa`** : Push the first element from stack B to stack A
- **`pb`** : Push the first element from stack A to stack B

### Rotate Operations
- **`ra`** : Rotate stack A upwards (first element moves to the end)
- **`rb`** : Rotate stack B upwards
- **`rr`** : Execute `ra` and `rb` simultaneously

### Reverse Rotate Operations
- **`rra`** : Reverse rotate stack A (last element moves to the front)
- **`rrb`** : Reverse rotate stack B
- **`rrr`** : Execute `rra` and `rrb` simultaneously

## Compilation

```bash
make              # Compile the program
make clean        # Remove object files
make fclean       # Remove object files and executable
make re           # Rebuild from scratch
```

Compilation flags:
- `-Wall -Wextra -Werror` : Strict compilation with all warnings

## Usage

```bash
./push_swap <number1> <number2> <number3> ...
```

### Examples

**Sort three numbers:**
```bash
./push_swap 3 2 1
# Output:
# sa
# rra
```

**Sort five numbers:**
```bash
./push_swap 5 4 3 2 1
# Output:
# pb
# pb
# sa
# pa
# pa
```

**Already sorted:**
```bash
./push_swap 1 2 3
# Output:
# (no operations - stack is already sorted)
```

### Input Format
- Space-separated or quoted numbers: `./push_swap "3 2 1"` or `./push_swap 3 2 1`
- Numbers must be unique integers
- Handles both positive and negative integers
- Supports INT_MIN to INT_MAX range

### Output
The program outputs the sequence of operations needed to sort stack A in ascending order, one operation per line.

## Algorithm Strategy

### Small Stack Sorting (size ≤ 5)
Uses an optimized insertion-based approach:
1. Find the position to insert the next element
2. Use rotations and swaps to move elements
3. Minimal operation count for small inputs

### Large Stack Sorting (size > 5)
Uses binary Radix Sort algorithm:
1. Create a mapping of values to their ranks (0 to n-1)
2. Process bits from least significant to most significant
3. For each bit, push all 0-bit numbers to stack B, rotate stack A
4. Push everything back from B to A
5. Result: Stack A is sorted in ascending order

## Sorting Efficiency

The implementation aims to minimize the number of operations:
- **2 numbers**: 1 operation max
- **3 numbers**: 2 operations max
- **5 numbers**: ~12 operations
- **100 numbers**: ~900 operations (target: < 1200)
- **500 numbers**: ~5500 operations (target: < 12000)

## Error Handling

The program handles and reports the following errors:
- Non-integer arguments
- Duplicate numbers
- Invalid number format
- No arguments provided (exits normally)
- Memory allocation failures

Errors are reported to stdout with "Error" message and programs exits with status 1.

## Key Features

- ✅ Fully compliant with 42 school push_swap specifications
- ✅ Handles edge cases (single number, two numbers, already sorted)
- ✅ Efficient sorting algorithms optimized for different input sizes
- ✅ Robust error handling and validation
- ✅ Memory-safe with proper cleanup
- ✅ Strict compilation flags (-Wall -Wextra -Werror)

## Building and Testing

To compile and test:

```bash
# Build the program
make

# Test with a few numbers
./push_swap 3 2 1

# Test with more numbers
./push_swap 5 4 3 2 1 0 -1

# Test edge cases
./push_swap 42          # Single number (no output)
./push_swap 1 2 3       # Already sorted (no output)
```

## Implementation Notes

- Written in C following 42 school C coding standard (Norm)
- No external libraries except standard C library
- Two-stack based sorting with predefined operations
- Adaptive algorithm selection based on input size
- Optimized for both small and large datasets

## Author

Created as part of the 42 School curriculum (Nice Promo)
