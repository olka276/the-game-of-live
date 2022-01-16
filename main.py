import validators
import board
from exceptions import MatrixNotSquareError
from neighbours import Neighbours

board_size = int(input('Type board size:'))
iterations_amount = int(input('Type interations amount:'))

board_matrix = board.create_random_binary_matrix(board_size)
neighbours_matrix = board.create_random_binary_matrix(board_size)

if not validators.is_matrix_square(board_matrix):
    raise MatrixNotSquareError

board.show(board_matrix, "Cell before starting")

n = Neighbours(neighbours_matrix, board_matrix)

# i - row, j - column. Y-axis is reversed on board.
for main in range(iterations_amount):
    for i in range(0, n.cells_matrix_size):
        for j in range(0, n.cells_matrix_size):
            if i == 0 and j == 0:
                n.left_bottom(i, j)

            elif i == 0 and j == n.cells_matrix_size - 1:
                n.right_bottom(i, j)

            elif i == n.cells_matrix_size - 1 and j == 0:
                n.left_top(i, j)

            elif i == n.cells_matrix_size - 1 and j == n.cells_matrix_size - 1:
                n.right_top(i, j)

            elif i == 0 and 0 < j < n.cells_matrix_size - 1:
                n.bottom(i, j)

            elif i == n.cells_matrix_size - 1 and 0 < j < n.cells_matrix_size - 1:
                n.top(i, j)

            elif 0 < i < n.cells_matrix_size - 1 and j == 0:
                n.left(i, j)

            elif 0 < i < n.cells_matrix_size - 1 and j == n.cells_matrix_size - 1:
                n.right(i, j)

            elif 0 < i < n.cells_matrix_size - 1 and 0 < i < n.cells_matrix_size - 1:
                n.other(i, j)

    for i in range(0, n.cells_matrix_size):
        for j in range(0, n.cells_matrix_size):
            n.is_alive(i, j)

    board.show(n.cells_matrix, "Iteration: %i" % main)
