class Matrix:
    def __init__(self, my_input1, my_input2):
        self.my_input1 = my_input1
        self.my_input2 = my_input2

    def __add__(self):
        new_matrix = [[1, 1, 1],
                      [2, 2, 2],
                      [3, 3, 3]]
        for i in range(len(self.my_input1)):

            for j in range(len(self.my_input2[i])):
                new_matrix[i][j] = self.my_input1[i][j] + self.my_input2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_matrix]))

        def __str__(self):
            return str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_matrix]))

my_matrix = Matrix([[1, 2, 3], #my_input1
                   [4, 5, 6],
                   [7, 8, 9]],

                   [[10, 11, 12], #my_input2
                   [13, 14, 15],
                   [16, 17, 18]])
print(my_matrix.__add__())