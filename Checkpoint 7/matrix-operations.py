def main():
    matrixxx = [[1, 1, 6, 5], 
                [8, 6, 9, 10], 
                [6, 4, 3, 4], 
                [5, 9, 9, 3]]
    row_sum(matrixxx, 0)
    col_sum(matrixxx, 1)
    change(matrixxx, 2, 3, 11)
    print(matrixxx)

def row_sum(matrix, row):
    print(sum(matrix[row]))

def col_sum(matrix, col):
    sum = 0
    for row in matrix:
        sum = sum + row[col]
    print(sum)

def change(matrix, row, col, new):
    matrix[row][col] = new

main()