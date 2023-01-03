def norm_matrix_to_plus(m1, m2):
    if len(m1) > len(m2):
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                matrix0 = [[0] * len(m1[i]) for _ in range(len(m1))]

        for i1 in range(len(m2)):
            for j1 in range(len(m2[i1])):
                matrix0[i1][j1] = matrix0[i1][j1] + m2[i1][j1]

        return matrix0, m1

    if len(m1) < len(m2):
        mf, mt = m2, m1
        for i in range(len(mf)):
            for j in range(len(mf[i])):
                matrix0 = [[0] * len(mf[i]) for _ in range(len(mf))]

        for i1 in range(len(mt)):
            for j1 in range(len(mt[i1])):
                matrix0[i1][j1] = matrix0[i1][j1] + mt[i1][j1]

        return matrix0, mf

    if len(m1) == len(m2):
        return m1, m2

def norm_matrix_to_minus(m1, m2):
    if len(m1) > len(m2):
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                matrix0 = [[0] * len(m1[i]) for _ in range(len(m1))]

        for i1 in range(len(m2)):
            for j1 in range(len(m2[i1])):
                matrix0[i1][j1] = matrix0[i1][j1] + m2[i1][j1]

        return m1, matrix0 # matrix0 = m2

    if len(m1) < len(m2):
        for i in range(len(m2)):
            for j in range(len(m2[i])):
                matrix0 = [[0] * len(m2[i]) for _ in range(len(m2))]

        for i1 in range(len(m1)):
            for j1 in range(len(m1[i1])):
                matrix0[i1][j1] = matrix0[i1][j1] + m1[i1][j1]

        return matrix0, m2 # matrix0 = m1



class Marix:
    def __init__(self, matrix):
        self.matrix = matrix


    def print_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()

##############################
# Multiplication by a number
##############################
    def mult_by_num(self, num):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j]*num, end=' ')
            print()

#############################
# Matrix transposition
#############################
    def transposition(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[j][i], end=' ')
            print()

############################
# Matrix Addition
############################

    def plus_matrix(self, matrix_to_plus):
        matrix_to_plus1, self.matrix = norm_matrix_to_plus(matrix_to_plus, self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j] + matrix_to_plus1[i][j], end=' ')
            print()

#########################
# Matrix Substraction
#########################
    def minus_matrix(self, matrix_to_minus):

        if len(self.matrix) > len(matrix_to_minus):
            self.matrix, matrix_to_minus1 = norm_matrix_to_minus(self.matrix, matrix_to_minus)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    print(self.matrix[i][j] - matrix_to_minus1[i][j], end=' ')
                print()

        elif len(self.matrix) < len(matrix_to_minus):
                self.matrix, matrix_to_minus1 = norm_matrix_to_minus(self.matrix, matrix_to_minus)
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[i])):
                        print(self.matrix[i][j] - matrix_to_minus1[i][j], end=' ')
                    print()

        elif len(self.matrix) == len(matrix_to_minus):
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[i])):
                        print(self.matrix[i][j] - matrix_to_minus[i][j], end=' ')
                    print()

##############################
# Matrix Multiplication
##############################
    def mult_by_matrix(self, matrix_to_multy):
        for n1 in range(len(self.matrix)):
            for m1 in range(len(self.matrix[n1])):
                n, m = len(self.matrix), len(self.matrix[n1])

        for m2 in range(len(matrix_to_multy)):
            for k2 in range(len(matrix_to_multy[m2])):
                m, k = len(matrix_to_multy), len(matrix_to_multy[m2])

        matrix0 = [[0] * int(k) for c in range(int(n))]
        for i in range(n):
            for j in range(k):
                for x in range(m):
                    matrix0[i][j] += self.matrix[i][x] * matrix_to_multy[x][j]

        for row in matrix0:
            print(*row)

        if n != k:
            raise SyntaxError('to multiply a matrix by a matrix - it is necessary that the number of rows = the number of columns!')




a = Marix([[6, 2, 1],
           [5, 44, 3],
           [7, 10, 91]])

print("The original matrix")
a.print_matrix()

print("Matrix Addition")
a.plus_matrix([[2, 1, 7],
                [13, 5, 6],
                [1, 8, 11]])

print("Matrix Substraction")
a.minus_matrix([[1, 5, 2],
                [4, 1, 0],
                [7, 3, 8]])

print("Multiplication by a number")
a.mult_by_num(8)

print("Matrix Multiplication")
a.mult_by_matrix([[2, 3, 4],
                [2, 6, 73],
                [5, 9, 1]])
print("Transpose matrix")
a.transposition()
