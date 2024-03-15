class MatrixOperations:
    def __init__(self, input_matrix):
        self.set_matrix(input_matrix) # Здесь п е р е д а ё м значение параметра matrix
        
    def set_matrix(self, matrix): # Здесь о б ъ я в л я е м параметр matrix
        try:
            self._GeneralValidation(matrix)
            self.__matrix = matrix # named started by "__" it is a privet. Can use only at this class
        except Exception as e:
            print(e)

    def _GeneralValidation(self, matrix): # name started by "_" is protected, can use only at this class and chhildes clss
        if type(matrix) is not list:
            raise Exception('Matrix "' + str(matrix)+ '" ' + 'must be a list')
            
        for i in range (len(matrix)):
            if type(matrix[i]) is not list:
                raise Exception('Matrix`s "' + str(matrix) + '" ' + 'columns is not a list')
            if len(matrix[i]) != len(matrix[0]):
                raise Exception('Matrix`s columns"' + str(matrix) + '" ' + ' have to be equals size')
            for j in range (len(matrix[i])):
                if type(matrix[i][j]) is not int:
                    raise Exception('Matrix`s element "' + str(i + 1) + str(j + 1) + ' of ' + str(matrix) + '" ' + ' have to be number')

    def __Validate_square_matrix(self, matrix):
        for x in range (len(matrix)):
            if len(matrix[0]) != len(matrix[x]):
                raise Exception('Matrix "' + str(matrix) + '" ' + ' is not square')

    def __gauss_transform(self, matrix): # Encapsulated method for transform matrix to triangle matrix
        try:
            self.__Validate_square_matrix(matrix)
            
            n = len(matrix)

            for i in range(n-1):
                for j in range(i+1, n):
                    factor = -matrix[j][i] / matrix[i][i]
                    for k in range(i, n):
                        matrix[j][k] = matrix[j][k] + factor * matrix[i][k]
        
            return matrix
        except Exception as e:
            print(e)
    
    def get_matrix_state(self):
        try:
            if(hasattr(self, '_MatrixOperations__matrix')):
                print('self.__matrix is exsistent')
            else:
                raise Exception('self.__matrix is no exsistent')

            return self.__gauss_transform(self.__matrix)
        except Exception as e:
            print(e)

class Determinant(MatrixOperations):
    def __init__(self, matrix):
        self.set_matrix(matrix)

    def set_matrix(self, matrix):
        super()._GeneralValidation(matrix)
        self.__matrix = matrix

    def Determinant_calc(self):
        super().__Validate_square_matrix(self.__matrix)
        
        det = 1
        transformed_matrix = super().__gauss_transform()

        for i in range(len(transformed_matrix)):
            det *= transformed_matrix[i][i]

        if det == -0.0:
            det = 0.0

        return det
    
class Boundry_extend_matrix(MatrixOperations):
    def __init__(self, matrix, x = None):
        super().set_matrix(matrix)
        self.x = x

    def matrix_extend(self, matrix, x):
        print(self.__matrix)

        x=int(x)
        extended_matrix = [ [0] * len(matrix[0])*x for _ in range(len(matrix)*x) ] #creates a new matrix full of zeroes with new dimentions

        rows = int(len(matrix))
        cols = int(len(matrix[0]))

        for z in range (x):
            for y in range (x):
                for i in range (rows):
                    for j in range (cols):
                        extended_matrix[i + z * rows][j + y * cols] = matrix[i][j]

        return (extended_matrix)
    
class two_matrix_operations(MatrixOperations):
    def __init__(matrix_A, matrix_B):
        super(matrix_A)._GeneralValidation(matrix_A)
        super(matrix_B)._GeneralValidation(matrix_B)

    def __mult_validate(self):
        if len(self.matrix_A[0]) != len(self.matrix_B):                             #direct validation
            raise ValueError("Cannot multiply matrices - wrong size")