def transpose(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    transposed_matrix = [[0 for _ in range(num_rows)] for _ in range(num_columns)]
    
    # Performing the transpose
    for i in range(num_rows):
        for j in range(num_columns):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix

# Example matrix
my_matrix = [[2, 3, 4], [8, 5, 1]]

# Getting the transposed result
transposed_result = transpose(my_matrix)

# Printing the transposed matrix
print(transposed_result)
