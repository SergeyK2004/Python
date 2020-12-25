class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        string = ''
        for row in self.data:
            string += str(row) + '\n'
        return string

    def __add__(self, other):
        min_len = min(len(self.data), len(other.data))
        new_matrix = []
        for i in range(min_len):
            new_list = []
            for num1, num2 in zip(self.data[i], other.data[i]):
                new_list.append(num1 + num2)
            new_matrix.append(new_list)
        return Matrix(new_matrix)

mat1 = Matrix([[1,2,3,4, 5], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2]])
mat2 = Matrix([[4,3,2,1], [2, 2, 2, 2]])
new_mat = mat1 + mat2

print('матрица №1')
print(mat1)
print('матрица №2')
print(mat2)
print('Сумма двух матриц')
print(new_mat)
