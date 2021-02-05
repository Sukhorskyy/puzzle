'''
Puzzle game
The program checks whether the entered combination is winning
Repository address on GitHub: https://github.com/Sukhorskyy/puzzle.git
'''

def read_board(board):
    '''
    (list) -> list
    Return a list of chars
    >>> print(read_board(["**** ****"]))
    [['*', '*', '*', '*', ' ', '*', '*', '*', '*']]
    >>> print(read_board(["  8  2***"]))
    [[' ', ' ', '8', ' ', ' ', '2', '*', '*', '*']]
    '''
    for i in range(len(board)):
        board[i] = list(board[i])
    return board


def horisontal(board):
    '''
    (list) -> bool
    Check whether the numbers repeat in row
    >>> myboard = ["**** ****","***1 ****","**  3****","* 4 1****","     9 5 ",\
        " 6  83  *","3   1  **","  8  2***","  2  ****"]
    >>> print(horisontal(myboard))
    True
    '''
    for i in range(len(board)):
        board[i] = list(filter(lambda element: element != '*', board[i]))
        board[i] = list(filter(lambda element: element != ' ', board[i]))
        board[i] = list(filter(lambda element: 0 <= int(element) <= 9, board[i]))
        if len(set(board[i])) != len(board[i]):
            return False
    return True


def vertical(board):
    '''
    (list) -> bool
    Check whether the numbers repeat in column
    >>> myboard = ["**** ****","***1 ****","**  3****","* 4 1****","     9 5 ",\
        " 6  83  *","3   1  **","  8  2***","  2  ****"]
    >>> print(vertical(myboard))
    False
    '''
    new_board = [[0 for i in range(len(board))] for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            new_board[i][j] = board[j][i]
    result = horisontal(new_board)
    return result


def color(board):
    '''
    (list) -> bool
    Check whether the numbers repeat in the cells of the same color
    >>> myboard = ["**** ****","***1 ****","**  3****","* 4 1****","     9 5 ",\
        " 6  83  *","3   1  **","  8  2***","  2  ****"]
    >>> print(color(myboard))
    True
    '''
    j = 0
    for i in range(8, 3, -1):
        first_part = []
        second_part = []
        for k in range(5):
            first_part.append(board[i-k][j])
            second_part.append(board[i][k+j])
        del second_part[0]
        color = first_part + second_part
        color = list(filter(lambda element: element != ' ', color))
        if len(set(color)) != len(color):
            return False
        j = j + 1
    return True


def validate_board(board):
    '''
    (list) -> bool
    Check whether the numbers satisfy all the conditions of the game
    >>> myboard = ["**** ****","***1 ****","**  3****","* 4 1****","     9 5 ",\
        " 6  83  *","3   1  **","  8  2***","  2  ****"]
    >>> print(validate_board(myboard))
    False
    '''
    board = read_board(board)
    if vertical(board) == False:
        return False
    if color(board)  == False:
        return False
    if horisontal(board) == False:
        return False
    return True
