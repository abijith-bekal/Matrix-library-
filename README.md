# Matrix Calculator (C Program)

This is a simple command-line **Matrix Calculator** written in C that allows users to perform various matrix operations such as:

- Addition
- Subtraction
- Multiplication
- Transpose
- Trace (only for square matrices)
- Determinant (2x2 and 3x3 square matrices)
- Inverse (2x2 and 3x3 square matrices)

## Features

- Supports matrix sizes up to 10x10.
- User-friendly prompts and input validation.
- Loop-based interface for multiple operations in one run.
- Handles matrix validation like dimension matching for operations like multiplication and square matrix checks for trace, determinant, and inverse.

## Operations Explained

1. **Addition / Subtraction**
   - Requires two matrices of the same dimensions.
2. **Multiplication**
   - Number of columns in the first matrix must match the number of rows in the second.
3. **Transpose**
   - Flips the matrix over its diagonal.
4. **Trace**
   - Sum of diagonal elements of a square matrix.
5. **Determinant**
   - Implemented for 2x2 and 3x3 matrices only.
6. **Inverse**
   - Implemented for 2x2 and 3x3 matrices only. Fails if the determinant is zero.

## How to Compile and Run

```bash
gcc matrix_calculator.c -o matrix_calculator
./matrix_calculator

## Example
Choose operation:
1. Addition
2. Subtraction
3. Multiplication
4. Transpose
5. Trace
6. Determinant
7. Inverse
Enter your choice: 1

Enter rows and columns for the matrices: 2 2
Enter matrix elements (2 x 2):
Element [1][1]: 1
Element [1][2]: 2
Element [2][1]: 3
Element [2][2]: 4
...
Result:
2.00    4.00
6.00    8.00

