class MatrixOperations:
    def __init__(self, matrix):
        self.__set_matrix(matrix)

    def __GeneralValidation(self, matrix):    
        if type(matrix) is not list:
            print(matrix, "Matrix must be a list")
        else:
            for x in range (len(matrix)):
                if type(matrix[x]) is not list:
                    print(matrix[x], "Matrix must be a list")
                    break                
                if len(matrix[0]) != len(matrix[x]):
                    print(matrix, "Matrix arrows must be the same size")
                    break
    
    def __Validate_square_matrix(self, matrix):
        for x in range (len(matrix)):
            if len(matrix[0]) != len(matrix[x]):
                raise ValueError("Matrix is not square")
        
        return matrix
    
    def __set_matrix(self, matrix):
       self.__GeneralValidation(matrix)
       self.__matrix = matrix

    def get_matrix_state(self):  
        return self.__matrix