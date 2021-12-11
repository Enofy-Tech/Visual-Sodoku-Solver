from src.sudoku_board import SudokuBoard

sudoku_board = SudokuBoard()
print(sudoku_board.board)
sudoku_board.display_board()
sudoku_board.solve_board()
sudoku_board.display_board()
print(sudoku_board.board)
