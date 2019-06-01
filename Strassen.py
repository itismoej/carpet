def RGB_To_Hex(RGB_Tuple):
    return '#{:02x}{:02x}{:02x}'.format( RGB_Tuple[0], RGB_Tuple[1]  , RGB_Tuple[2] )


def Hex_To_RGB(Hex_Value):
    Hex_Value=Hex_Value.lstrip("#")
    return tuple(int(Hex_Value[i:i+2], 16) for i in (0, 2, 4))


def TwoxTwo_Matrix_Multiplication(a, b):
    """
    Only for 2x2 matrices

    Modified For Multiplying RGB Values

    | a1 a2 |	| b1 b2 |
    | a3 a4 | 	| b3 b4 |

    """




    new_matrix = [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                  [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

    return new_matrix


def Add_Two_Matrix(matrix_a, matrix_b):
    # print(matrix_a)
    return [[matrix_a[row][col] + matrix_b[row][col]
             for col in range(len(matrix_a[row]))] for row in range(len(matrix_a))]


def Subtract_Two_Matrix(matrix_a, matrix_b):
    return [[matrix_a[row][col] - matrix_b[row][col]
             for col in range(len(matrix_a[row]))] for row in range(len(matrix_a))]


def Split_Matrix_To_4_Parts(a):
    """
    Given a matrix, return the TOP_LEFT, TOP_RIGHT, BOT_LEFT and BOT_RIGHT quadrant
    """


    matrix_length = len(a)
    mid = matrix_length // 2
    top_left = [[a[i][j] for j in range(mid)] for i in range(mid)]
    bot_left = [[a[i][j] for j in range(mid)] for i in range(mid, matrix_length)]

    top_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid)]
    bot_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid, matrix_length)]

    return top_left, top_right, bot_left, bot_right


def get_matrix_dimensions(matrix):
    return len(matrix), len(matrix[0])


def Strassen(matrix_a, matrix_b):

    if get_matrix_dimensions(matrix_a) == (2, 2):
        return TwoxTwo_Matrix_Multiplication(matrix_a, matrix_b)

    A, B, C, D = Split_Matrix_To_4_Parts(matrix_a)
    E, F, G, H = Split_Matrix_To_4_Parts(matrix_b)

    p1 = Strassen(A, Subtract_Two_Matrix(F, H))
    p2 = Strassen(Add_Two_Matrix(A, B), H)
    p3 = Strassen(Add_Two_Matrix(C, D), E)
    p4 = Strassen(D, Subtract_Two_Matrix(G, E))
    p5 = Strassen(Add_Two_Matrix(A, D), Add_Two_Matrix(E, H))
    p6 = Strassen(Subtract_Two_Matrix(B, D), Add_Two_Matrix(G, H))
    p7 = Strassen(Subtract_Two_Matrix(A, C), Add_Two_Matrix(E, F))

    top_left = Add_Two_Matrix(Subtract_Two_Matrix(Add_Two_Matrix(p5, p4), p2), p6)
    top_right = Add_Two_Matrix(p1, p2)
    bot_left = Add_Two_Matrix(p3, p4)
    bot_right = Subtract_Two_Matrix(Subtract_Two_Matrix(Add_Two_Matrix(p1, p5), p3), p7)

    # construct the new matrix from our 4 quadrants
    new_matrix = []
    for i in range(len(top_right)):
        new_matrix.append(top_left[i] + top_right[i])
    for i in range(len(bot_right)):
        new_matrix.append(bot_left[i] + bot_right[i])
    return new_matrix

a=[[2,1,5,0],[3,1,0,0],[3,1,5,5]]
b=[[1,1,4,0],[4,2,9,0],[8,5,1,9]]
a.append([0,0,0,0])
b.append([0,0,0,0])
print(Strassen(a,b))


