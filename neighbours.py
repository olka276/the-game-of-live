class Neighbours:
    def __init__(self, neighbours_matrix, board):
        self.neighbours_alive_matrix = neighbours_matrix
        self.alive = 0
        self.cells_matrix = board
        self.cells_matrix_size = len(self.cells_matrix)

    def left_top(self, i, j):
        self.alive = 0
        for x in range(self.cells_matrix_size - 2, self.cells_matrix_size):
            for y in range(0, 2):
                self.alive = self.alive + self.cells_matrix[x][y]
        self.neighbours_alive_matrix[i][j] = self.alive - self.cells_matrix[i][j]

    def right_top(self, i, j):
        self.alive = 0
        for x in range(self.cells_matrix_size - 2, self.cells_matrix_size):
            for y in range(self.cells_matrix_size - 2, self.cells_matrix_size):
                self.alive = self.alive + self.cells_matrix[x][y]
        self.neighbours_alive_matrix[i][j] = self.alive - self.cells_matrix[i][j]

    def left_bottom(self, i, j):
        self.alive = 0
        for x in range(0, 2):
            for y in range(0, 2):
                self.alive = self.alive + self.cells_matrix[x][y]
        self.neighbours_alive_matrix[i][j] = self.alive - self.cells_matrix[i][j]

    def right_bottom(self, i, j):
        self.alive = 0
        for x in range(0, 2):
            for y in range(self.cells_matrix_size - 2, self.cells_matrix_size):
                self.alive = self.alive + self.cells_matrix[x][y]
        self.neighbours_alive_matrix[i][j] = self.alive - self.cells_matrix[i][j]

    def top(self, i, j):
        self.alive = 0
        for x in range(self.cells_matrix_size - 2, self.cells_matrix_size):
            for y in range(j - 1, j + 2):
                self.alive = self.alive + self.cells_matrix[x][y]
        self.neighbours_alive_matrix[i][j] = self.alive - self.cells_matrix[i][j]

    def bottom(self, i, j):
        self.alive = 0
        for x in range(0, 2):
            for y in range(j - 1, j + 2):
                self.alive = self.alive + self.cells_matrix[x][y]
        self.neighbours_alive_matrix[i][j] = self.alive - self.cells_matrix[i][j]

    def left(self, i, j):
        self.alive = 0
        for x in range(i - 1, i + 2):
            for y in range(0, 2):
                self.alive = self.alive + self.cells_matrix[x][y]
        self.neighbours_alive_matrix[i][j] = self.alive - self.cells_matrix[i][j]

    def right(self, i, j):
        self.alive = 0
        for x in range(i - 1, i + 2):
            for y in range(self.cells_matrix_size - 2, self.cells_matrix_size):
                self.alive = self.alive + self.cells_matrix[x][y]
        self.neighbours_alive_matrix[i][j] = self.alive - self.cells_matrix[i][j]

    def other(self, i, j):
        self.alive = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                self.alive = self.alive + self.cells_matrix[x][y]
        self.neighbours_alive_matrix[i][j] = self.alive - self.cells_matrix[i][j]

    def is_alive(self, i, j):
        if self.cells_matrix[i][j] == 0 and self.neighbours_alive_matrix[i][j] == 3:
            self.cells_matrix[i][j] = 1
        if self.cells_matrix[i][j] == 1 and self.neighbours_alive_matrix[i][j] < 2:
            self.cells_matrix[i][j] = 0
        if self.cells_matrix[i][j] == 1 and 2 <= self.neighbours_alive_matrix[i][j] <= 3:
            self.cells_matrix[i][j] = 1
        if self.cells_matrix[i][j] == 1 and self.neighbours_alive_matrix[i][j] > 3:
            self.cells_matrix[i][j] = 0
