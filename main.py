from Classes.MatrixOperations_G_2 import MatrixOperations, Boundry_extend_matrix, Two_matrix_operations

text = "MATRIX IS"
matrix = [[1, 2, 4, 5], [4, 5, 6, 3], [1, 3, 5, 3]]

matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_B = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

try:
    A = MatrixOperations(matrix) #parent class
    #C = MatrixOperations(text)

    A_get_result = A.get_matrix_state()

    if(A_get_result): print()

    B = Boundry_extend_matrix([[1, 2, 4], [4, 5, 6], [7, 8, 9]], 2) #child class

    print(B.matrix_extend())

    matrix_obj = Two_matrix_operations(matrix_A, matrix_B)

    print(matrix_obj.matrix_addition())
    print(matrix_obj.matrix_multiply())
except Exception as e:
    print(e)