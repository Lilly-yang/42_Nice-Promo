*This project has been created as part of the 42 curriculum by lyang.*

# push_swap

## Description

`push_swap` is a sorting project from the 42 curriculum. The goal is to sort a list of integers using only a restricted set of stack operations while producing as few instructions as possible.

The program takes a sequence of integers, validates the input, stores the values in two stacks, and prints the operations needed to transform stack A into sorted order. The challenge is not only to sort correctly, but also to choose strategies that keep the operation count reasonably low for different input sizes.

This implementation uses three sorting paths:

- a small-stack strategy for 2 to 5 values,
- a chunk-based strategy for medium-sized inputs,
- a radix-based strategy for larger inputs.

## Instructions

### Compilation

From the `push_swap/` directory, build the project with:

```sh
make
```

This produces the `push_swap` executable.

To remove generated objects and the executable:

```sh
make clean
make fclean
make re
```

### Execution

Run the program with a list of integers, either as separate arguments or as a single quoted string:

```sh
./push_swap 3 2 1
./push_swap "3 2 1"
```

The program prints the sequence of allowed operations on standard output.

### Input rules

- Only valid integers are accepted.
- Duplicate values are rejected.
- Values must fit in the 32-bit signed integer range.
- Empty arguments and malformed tokens are treated as errors.

### Operation set

The project relies on the classic push_swap operations:

- `sa`, `sb`, `ss`
- `pa`, `pb`
- `ra`, `rb`, `rr`
- `rra`, `rrb`, `rrr`

## Algorithm Choices

The implementation selects the sorting strategy according to the number of values:

### 1. Small-stack strategy for 2 to 5 values

For very small inputs, a specialized approach is more efficient than a generic algorithm.

For 2 values, the solution is trivial: swap only when the pair is in descending order.

For 3 values, the code checks the relative order of the top three elements and applies the shortest combination of swap, rotate, and reverse-rotate operations needed to sort them.

For 4 and 5 values, the algorithm repeatedly moves the minimum value to the top with the cheapest rotation direction, pushes it to stack B, sorts the remaining 3 values, and then pushes the saved values back to stack A.

Why this choice:

- It minimizes overhead on tiny inputs.
- It avoids the complexity of a larger algorithm when the entire problem fits into a few direct cases.
- It keeps the operation count low and predictable.

### 2. Chunk-based strategy for medium inputs

For inputs up to 100 values, the program uses a chunking approach after coordinate compression.

Coordinate compression remaps the original integers to the range `0..n-1`. This makes comparisons simpler and avoids issues with negative values or large numeric ranges.

The compressed range is then split into chunks. Values belonging to the current chunk are pushed from stack A to stack B. During this phase, values in the lower half of the current chunk are rotated inside stack B so that the structure of B remains more favorable for reconstruction.

Once all values are moved to stack B, the algorithm repeatedly finds the maximum value in B, rotates B in the shortest direction to bring it to the top, and pushes it back to A. This restores ascending order in A.

Why this choice:

- It is more adaptive than plain radix sorting for mid-sized inputs.
- It reduces the number of unnecessary operations compared with a naive push-all-then-sort approach.
- The chunk size can be tuned for the input range, which balances efficiency and implementation simplicity.

### 3. Radix strategy for large inputs

For larger inputs, the program uses binary radix sort on the compressed values.

After compression, the algorithm processes the input bit by bit. For each bit position, values with a `0` in that position are pushed to B, and values with a `1` are rotated in A. After one full pass, all values are pushed back from B to A. The process repeats for every bit required to represent `n - 1`.

Why this choice:

- It is deterministic and easy to reason about.
- It scales well to larger input sizes.
- Its complexity is predictable, which is useful when the number of operations must remain controlled.

### General design decisions

- Two stacks are used because the subject restricts the available workspace to stack operations.
- The secondary stack is preallocated to the full input size, which avoids repeated reallocations during sorting.
- Compression is used before the chunk and radix paths so that both algorithms work on a compact, ordered index space.
- The program exits early when the input is already sorted, avoiding unnecessary work.

## Resources

Classic references used while building and documenting this project:

- 42 push_swap subject and evaluation guidelines.
- The `strtol(3)` man page for strict integer parsing and overflow handling.
- Introductory references on binary radix sort.
- General articles and tutorials on stack-based sorting strategies and push_swap optimization.

### AI usage

AI was used to draft and structure this README, refine the wording of the algorithm explanations, and check that the documented behavior matched the implementation strategy in the source code.

AI was not used to generate the sorting logic itself. The code remains the result of the project implementation.

## Usage Example

```sh
./push_swap 4 67 3 87 23
```

The program prints the operations required to sort the input in ascending order.