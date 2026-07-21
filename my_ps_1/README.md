*This project has been created as part of the 42 curriculum by lyang, ylecain.*

# push_swap

## Description

`push_swap` is a 42 sorting project.
The goal is to sort a list of integers in ascending order using only the allowed stack operations on two stacks, `a` and `b`, while keeping the number of operations as low as possible.

This implementation includes the mandatory program `push_swap` and supports the four strategy modes required by the subject:
- `--simple`
- `--medium`
- `--complex`
- `--adaptive`

It also supports the mandatory benchmark mode:
- `--bench`

## Contributors

- `lyang`: original project structure, stack operations, and initial sorting base.
- `ylecain`: parser cleanup, strategy selection fixes, adaptive mode based on disorder, benchmark integration, Makefile fixes, testing, and documentation updates.

## Instructions

### Compilation

Build the project with:

```sh
make
```

### Cleanup

Remove object files:

```sh
make clean
```

Remove object files and the binary:

```sh
make fclean
```

Rebuild everything:

```sh
make re
```

## Execution

Run the program with a list of integers:

```sh
./push_swap 3 2 1
```

You can also pass the numbers as a single quoted string:

```sh
./push_swap "3 2 1"
```

Force a specific strategy:

```sh
./push_swap --simple 5 4 3 2 1
./push_swap --medium 4 67 3 87 23
./push_swap --complex 4 67 3 87 23
./push_swap --adaptive 4 67 3 87 23
```

Run with benchmark mode enabled:

```sh
./push_swap --bench --adaptive 4 67 3 87 23
```

## Output behavior

- The list of sorting operations is printed to `stdout`.
- Benchmark information is printed to `stderr` only when `--bench` is used.
- If no arguments are provided, the program prints nothing.
- On error, the program prints `Error` followed by `\n` on `stderr`.

## Input rules

The program accepts:
- valid signed 32-bit integers,
- either split arguments or a single quoted string.

The program rejects:
- duplicate values,
- non-numeric tokens,
- values outside the `int` range,
- empty or malformed arguments.

## Allowed operations

The project uses the standard push_swap instruction set:
- `sa`, `sb`, `ss`
- `pa`, `pb`
- `ra`, `rb`, `rr`
- `rra`, `rrb`, `rrr`

## Algorithm choices

### 1. Simple strategy — `--simple`

The simple strategy is an `O(n^2)` method.
It repeatedly brings the minimum value to the top of stack `a`, pushes it to stack `b`, sorts the remaining small set directly, and then pushes everything back to `a`.

This strategy is suitable for very small or almost trivial inputs.

### 2. Medium strategy — `--medium`

The medium strategy is a chunk-based `O(n*sqrt(n))` style method.
Before sorting, values are compressed into ranks from `0` to `n - 1`.
The input is then processed in chunks whose size is close to `sqrt(n)`.
Values belonging to the current range are pushed to `b`, and stack `b` is partially rotated to improve reconstruction.

This strategy is intended for medium-sized inputs.

### 3. Complex strategy — `--complex`

The complex strategy is a radix-based `O(n log n)` method on compressed ranks.
It processes the numbers bit by bit, pushing values with a `0` bit to `b` and rotating values with a `1` bit in `a`, then restoring everything back to `a` after each pass.

This strategy is intended for large inputs.

### 4. Adaptive strategy — `--adaptive`

The adaptive strategy is the default behavior when no strategy flag is provided.
It computes the disorder of stack `a` before any move and selects the internal strategy according to the subject thresholds:
- if `disorder < 0.2`, it uses the simple strategy,
- if `0.2 <= disorder < 0.5`, it uses the medium strategy,
- if `disorder >= 0.5`, it uses the complex strategy.

## Disorder metric

Disorder measures how far the initial stack is from being sorted.
It is computed as:

- number of inverted pairs / total number of pairs

A fully sorted stack has a disorder of `0`.
A highly reversed stack approaches `1`.

## Benchmark mode

When `--bench` is enabled, the program prints the following information to `stderr` after sorting:
- disorder percentage with two decimal places,
- the strategy actually used,
- its theoretical complexity class,
- the total number of operations,
- the count of each operation type:
  - `sa`, `sb`, `ss`
  - `pa`, `pb`
  - `ra`, `rb`, `rr`
  - `rra`, `rrb`, `rrr`

## Example

```sh
ARG="4 67 3 87 23"
./push_swap --adaptive $ARG | ./checker_linux $ARG
```

Expected result:

```sh
OK
```

## Resources

Useful references related to the project:
- the official 42 `push_swap` subject,
- algorithm complexity references,
- radix sort references,
- chunk-based push_swap resources,
- general documentation about stack-based sorting.

## AI usage

AI was used to:
- audit the repository against the subject,
- identify inconsistencies between source files, prototypes, and the Makefile,
- help reorganize and rewrite the documentation,
- assist with planning and validating corrections.

All generated suggestions were reviewed, tested, and adapted manually before being kept in the project.
