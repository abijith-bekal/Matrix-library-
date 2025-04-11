#include <stdio.h>

#define MAX 10 // Maximum matrix size

void inputMatrix(float matrix[MAX][MAX], int row, int col) {
    printf("Enter matrix elements (%d x %d):\n", row, col);
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            printf("Element [%d][%d]: ", i + 1, j + 1);
            scanf("%f", &matrix[i][j]);
        }
    }
}

void printMatrix(float matrix[MAX][MAX], int row, int col) {
    printf("Result:\n");
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            printf("%.2f\t", matrix[i][j]);
        }
        printf("\n");
    }
}

void addMatrix(float A[MAX][MAX], float B[MAX][MAX], float result[MAX][MAX], int row, int col) {
    for (int i = 0; i < row; i++)
        for (int j = 0; j < col; j++)
            result[i][j] = A[i][j] + B[i][j];
}

void subtractMatrix(float A[MAX][MAX], float B[MAX][MAX], float result[MAX][MAX], int row, int col) {
    for (int i = 0; i < row; i++)
        for (int j = 0; j < col; j++)
            result[i][j] = A[i][j] - B[i][j];
}

void multiplyMatrix(float A[MAX][MAX], float B[MAX][MAX], float result[MAX][MAX], int row1, int col1, int col2) {
    for (int i = 0; i < row1; i++)
        for (int j = 0; j < col2; j++) {
            result[i][j] = 0;
            for (int k = 0; k < col1; k++)
                result[i][j] += A[i][k] * B[k][j];
        }
}

void transposeMatrix(float matrix[MAX][MAX], float transposed[MAX][MAX], int row, int col) {
    for (int i = 0; i < row; i++)
        for (int j = 0; j < col; j++)
            transposed[j][i] = matrix[i][j];
}

int traceMatrix(float matrix[MAX][MAX], int size) {
    int trace = 0;
    for (int i = 0; i < size; i++)
        trace += matrix[i][i];
    return trace;
}

float determinant(float matrix[MAX][MAX], int n) {
    if (n == 2) {
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
    } else if (n == 3) {
        return matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
               - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
               + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);
    }
    return 0;
}

int inverseMatrix(float matrix[MAX][MAX], float inverse[MAX][MAX], int n) {
    float det = determinant(matrix, n);
    if (det == 0) {
        printf("Matrix is singular, inverse does not exist.\n");
        return 0;
    }

    if (n == 2) {
        inverse[0][0] = matrix[1][1] / det;
        inverse[0][1] = -matrix[0][1] / det;
        inverse[1][0] = -matrix[1][0] / det;
        inverse[1][1] = matrix[0][0] / det;
    } else if (n == 3) {
        float invDet = 1.0 / det;
        inverse[0][0] = (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) * invDet;
        inverse[0][1] = (matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]) * invDet;
        inverse[0][2] = (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) * invDet;

        inverse[1][0] = (matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]) * invDet;
        inverse[1][1] = (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) * invDet;
        inverse[1][2] = (matrix[0][2] * matrix[1][0] - matrix[0][0] * matrix[1][2]) * invDet;

        inverse[2][0] = (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]) * invDet;
        inverse[2][1] = (matrix[0][1] * matrix[2][0] - matrix[0][0] * matrix[2][1]) * invDet;
        inverse[2][2] = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) * invDet;
    }
    return 1;
}

int main() {
    float A[MAX][MAX], B[MAX][MAX], result[MAX][MAX], inverse[MAX][MAX];
    int row1, col1, row2, col2, choice, repeat, matrixChoice, n;

    do {
        printf("\nChoose operation:\n");
        printf("1. Addition\n2. Subtraction\n3. Multiplication\n4. Transpose\n5. Trace\n6. Determinant\n7. Inverse\n");
        printf("Enter your choice: ");
        while (scanf("%d", &choice) != 1 || (choice < 1 || choice > 7)) {
            printf("Invalid choice! Please enter a number between 1 and 7.\n");
            while (getchar() != '\n'); // Clear input buffer
        }

        if (choice == 1 || choice == 2) { // Addition or Subtraction
            printf("Enter rows and columns for the matrices: ");
            scanf("%d %d", &row1, &col1);
            row2 = row1, col2 = col1; // Same dimensions required
            inputMatrix(A, row1, col1);
            inputMatrix(B, row2, col2);
        }
        else if (choice == 3) { // Multiplication
            printf("Enter rows and columns for first matrix: ");
            scanf("%d %d", &row1, &col1);
            printf("Enter rows and columns for second matrix: ");
            scanf("%d %d", &row2, &col2);
            if (col1 != row2) {
                printf("Multiplication not possible. Column count of first matrix must match row count of second.\n");
                continue;
            }
            inputMatrix(A, row1, col1);
            inputMatrix(B, row2, col2);
        }
        else { // Transpose, Trace, Determinant, or Inverse
            printf("Enter rows and columns for matrix: ");
            scanf("%d %d", &row1, &col1);
            inputMatrix(A, row1, col1);
        }

        switch (choice) {
            case 1: // Addition
                addMatrix(A, B, result, row1, col1);
                printMatrix(result, row1, col1);
                break;
            case 2: // Subtraction
                subtractMatrix(A, B, result, row1, col1);
                printMatrix(result, row1, col1);
                break;
            case 3: // Multiplication
                multiplyMatrix(A, B, result, row1, col1, col2);
                printMatrix(result, row1, col2);
                break;
            case 4: // Transpose
                transposeMatrix(A, result, row1, col1);
                printMatrix(result, col1, row1);
                break;
            case 5: // Trace
                if (row1 == col1) {
                    printf("Trace: %d\n", traceMatrix(A, row1));
                } else {
                    printf("Trace is only defined for square matrices.\n");
                }
                break;
            case 6: // Determinant
                if (row1 == col1) {
                    float det = determinant(A, row1);
                    printf("Determinant: %.2f\n", det);
                } else {
                    printf("Determinant is only defined for square matrices.\n");
                }
                break;
            case 7: // Inverse
                if (row1 == col1) {
                    int status = inverseMatrix(A, result, row1);
                    if (status) {
                        printMatrix(result, row1, col1);
                    }
                } else {
                    printf("Inverse is only defined for square matrices.\n");
                }
                break;
        }

        printf("\nPerform another operation? (1 for Yes, 0 for No): ");
        while (scanf("%d", &repeat) != 1 || (repeat != 0 && repeat != 1)) {
            printf("Invalid input! Enter 1 to continue or 0 to exit.\n");
            while (getchar() != '\n');
        }

    } while (repeat);

    printf("Exiting program...\n");
    return 0;
}#include <stdio.h>

#define MAX 10 // Maximum matrix size

void inputMatrix(float matrix[MAX][MAX], int row, int col) {
    printf("Enter matrix elements (%d x %d):\n", row, col);
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            printf("Element [%d][%d]: ", i + 1, j + 1);
            scanf("%f", &matrix[i][j]);
        }
    }
}

void printMatrix(float matrix[MAX][MAX], int row, int col) {
    printf("Result:\n");
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            printf("%.2f\t", matrix[i][j]);
        }
        printf("\n");
    }
}

void addMatrix(float A[MAX][MAX], float B[MAX][MAX], float result[MAX][MAX], int row, int col) {
    for (int i = 0; i < row; i++)
        for (int j = 0; j < col; j++)
            result[i][j] = A[i][j] + B[i][j];
}

void subtractMatrix(float A[MAX][MAX], float B[MAX][MAX], float result[MAX][MAX], int row, int col) {
    for (int i = 0; i < row; i++)
        for (int j = 0; j < col; j++)
            result[i][j] = A[i][j] - B[i][j];
}

void multiplyMatrix(float A[MAX][MAX], float B[MAX][MAX], float result[MAX][MAX], int row1, int col1, int col2) {
    for (int i = 0; i < row1; i++)
        for (int j = 0; j < col2; j++) {
            result[i][j] = 0;
            for (int k = 0; k < col1; k++)
                result[i][j] += A[i][k] * B[k][j];
        }
}

void transposeMatrix(float matrix[MAX][MAX], float transposed[MAX][MAX], int row, int col) {
    for (int i = 0; i < row; i++)
        for (int j = 0; j < col; j++)
            transposed[j][i] = matrix[i][j];
}

int traceMatrix(float matrix[MAX][MAX], int size) {
    int trace = 0;
    for (int i = 0; i < size; i++)
        trace += matrix[i][i];
    return trace;
}

float determinant(float matrix[MAX][MAX], int n) {
    if (n == 2) {
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
    } else if (n == 3) {
        return matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
               - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
               + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);
    }
    return 0;
}

int inverseMatrix(float matrix[MAX][MAX], float inverse[MAX][MAX], int n) {
    float det = determinant(matrix, n);
    if (det == 0) {
        printf("Matrix is singular, inverse does not exist.\n");
        return 0;
    }

    if (n == 2) {
        inverse[0][0] = matrix[1][1] / det;
        inverse[0][1] = -matrix[0][1] / det;
        inverse[1][0] = -matrix[1][0] / det;
        inverse[1][1] = matrix[0][0] / det;
    } else if (n == 3) {
        float invDet = 1.0 / det;
        inverse[0][0] = (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) * invDet;
        inverse[0][1] = (matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]) * invDet;
        inverse[0][2] = (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) * invDet;

        inverse[1][0] = (matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]) * invDet;
        inverse[1][1] = (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) * invDet;
        inverse[1][2] = (matrix[0][2] * matrix[1][0] - matrix[0][0] * matrix[1][2]) * invDet;

        inverse[2][0] = (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]) * invDet;
        inverse[2][1] = (matrix[0][1] * matrix[2][0] - matrix[0][0] * matrix[2][1]) * invDet;
        inverse[2][2] = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) * invDet;
    }
    return 1;
}

int main() {
    float A[MAX][MAX], B[MAX][MAX], result[MAX][MAX], inverse[MAX][MAX];
    int row1, col1, row2, col2, choice, repeat, matrixChoice, n;

    do {
        printf("\nChoose operation:\n");
        printf("1. Addition\n2. Subtraction\n3. Multiplication\n4. Transpose\n5. Trace\n6. Determinant\n7. Inverse\n");
        printf("Enter your choice: ");
        while (scanf("%d", &choice) != 1 || (choice < 1 || choice > 7)) {
            printf("Invalid choice! Please enter a number between 1 and 7.\n");
            while (getchar() != '\n'); // Clear input buffer
        }

        if (choice == 1 || choice == 2) { // Addition or Subtraction
            printf("Enter rows and columns for the matrices: ");
            scanf("%d %d", &row1, &col1);
            row2 = row1, col2 = col1; // Same dimensions required
            inputMatrix(A, row1, col1);
            inputMatrix(B, row2, col2);
        }
        else if (choice == 3) { // Multiplication
            printf("Enter rows and columns for first matrix: ");
            scanf("%d %d", &row1, &col1);
            printf("Enter rows and columns for second matrix: ");
            scanf("%d %d", &row2, &col2);
            if (col1 != row2) {
                printf("Multiplication not possible. Column count of first matrix must match row count of second.\n");
                continue;
            }
            inputMatrix(A, row1, col1);
            inputMatrix(B, row2, col2);
        }
        else { // Transpose, Trace, Determinant, or Inverse
            printf("Enter rows and columns for matrix: ");
            scanf("%d %d", &row1, &col1);
            inputMatrix(A, row1, col1);
        }

        switch (choice) {
            case 1: // Addition
                addMatrix(A, B, result, row1, col1);
                printMatrix(result, row1, col1);
                break;
            case 2: // Subtraction
                subtractMatrix(A, B, result, row1, col1);
                printMatrix(result, row1, col1);
                break;
            case 3: // Multiplication
                multiplyMatrix(A, B, result, row1, col1, col2);
                printMatrix(result, row1, col2);
                break;
            case 4: // Transpose
                transposeMatrix(A, result, row1, col1);
                printMatrix(result, col1, row1);
                break;
            case 5: // Trace
                if (row1 == col1) {
                    printf("Trace: %d\n", traceMatrix(A, row1));
                } else {
                    printf("Trace is only defined for square matrices.\n");
                }
                break;
            case 6: // Determinant
                if (row1 == col1) {
                    float det = determinant(A, row1);
                    printf("Determinant: %.2f\n", det);
                } else {
                    printf("Determinant is only defined for square matrices.\n");
                }
                break;
            case 7: // Inverse
                if (row1 == col1) {
                    int status = inverseMatrix(A, result, row1);
                    if (status) {
                        printMatrix(result, row1, col1);
                    }
                } else {
                    printf("Inverse is only defined for square matrices.\n");
                }
                break;
        }

        printf("\nPerform another operation? (1 for Yes, 0 for No): ");
        while (scanf("%d", &repeat) != 1 || (repeat != 0 && repeat != 1)) {
            printf("Invalid input! Enter 1 to continue or 0 to exit.\n");
            while (getchar() != '\n');
        }

    } while (repeat);

    printf("Exiting program...\n");
    return 0;
}