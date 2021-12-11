from typing import Union

from config import DEFAULT_ROW_LENGTH, DEFAULT_COLUMN_HEIGHT, DEFAULT_BOX_LENGTH, DEFAULT_BOX_HEIGHT


class SudokuBoard:
    def __init__(
            self,
            row_length: int = DEFAULT_ROW_LENGTH,
            column_length: int = DEFAULT_COLUMN_HEIGHT,
            box_length: int = DEFAULT_BOX_LENGTH,
            box_height: int = DEFAULT_BOX_HEIGHT
    ):
        self.row_length = row_length
        self.column_length = column_length
        self.box_length = box_length
        self.box_height = box_height
        self.board = self.generate_sudoku_puzzle()

    def generate_sudoku_puzzle(self) -> list[list[Union[int | None]]]:
        return [
            [1, 4, None, None, 3, None, None, None, None],
            [None, 8, 2, 6, None, None, None, None, 9],
            [7, None, None, None, None, 4, None, None, 5],
            [3, 2, None, None, 7, None, None, None, None],
            [None, None, 5, None, None, None, 1, 6, None],
            [None, None, None, 9, None, None, None, 2, 8],
            [6, None, 4, None, None, 1, None, 7, 2],
            [None, 1, None, None, 8, None, 3, None, None],
            [None, None, 9, None, None, None, 5, None, None]
        ]

    def display_board(self) -> None:
        pass

    def solve_board(self) -> bool:
        def find_empty(board: list[list[Union[int | None]]]) -> tuple[int, int]:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] is None:
                        return i, j

        empty_square = find_empty(self.board)
        if empty_square:
            row, column = empty_square
        else:
            return True

        for i in range(1, 10):
            if self.check_digit_is_valid(i, (row, column)):
                self.board[row][column] = i

                if self.solve_board():
                    return True

                self.board[row][column] = None

    def check_digit_is_valid(
            self,
            digit: int,
            digit_index: tuple[int, int]
    ) -> bool:
        # Check rows
        for i in range(len(self.board[0])):
            if self.board[digit_index[0]][i] == digit and digit_index[1] != i:
                return False

        # Check columns
        for i in range(len(self.board)):
            if self.board[i][digit_index[1]] == digit and digit_index[0] != i:
                return False

        # Check box
        box_x = digit_index[1] // self.box_length
        box_y = digit_index[0] // self.box_height

        for i in range(box_y * self.box_height, box_y * self.box_height + self.box_height):
            for j in range(box_x * self.box_length, box_x * self.box_length + self.box_length):
                if self.board[i][j] == digit and (i, j) != digit_index:
                    return False

        return True
