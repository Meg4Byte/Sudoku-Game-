#backtracking sudoku board

import random

class Board:

    def __init__(self , n : int):
        
        self.random_combination = list(range(1 , 10))
        random.shuffle(self.random_combination)
        self.board = [[0]*9 for _ in range(n)]
        self.board[random.randint(0  , 8 )] = self.random_combination

        #print(self.board)

    def get_sudoku_board(self) -> list[list[int]]:
        return self.board
    
    def set_row_col(self , row , col , num):
        self.board[row][col] = num

    def print_sudoku_board(self) -> None:
        for row in self.get_sudoku_board():
            print(row)
    
class SudokuSolver(Board):

    def __init__(self, n: int):
        super().__init__(n)

    def find_empty_cell(self):
        for i , row in enumerate(super().get_sudoku_board()):
            for j , item in enumerate(row):

                if item == 0:
                    return (i , j)
                
        return None
    
    def filling_spot(self , row , col , num):

        #check if the number is present in row or col
        for i in range(9):

            if self.get_sudoku_board()[row][i] == num or self.get_sudoku_board()[i][col] == num:
                return False

        #check if the number is present in sub box    
        start_row , start_col =  3 * (row // 3) , 3 * (col // 3)

        for i in range(3):
            for j in range(3):

                if self.get_sudoku_board()[start_row+i][start_col+j] == num:
                    return False
            
        return True

    def is_move_valid(self , board = None):
        
        #check if the board is solved
        if not self.find_empty_cell():
            #print("--------------")
            #self.print_sudoku_board()
            return True
        
        else:
            row , col = self.find_empty_cell()

            for num in range(1 , 10):

                if self.filling_spot(row , col , num):
                    self.set_row_col(row , col , num)
                    self.print_sudoku_board()
                    if self.is_move_valid():
                        return True

                    #this means that current combination is not valid so try next number
                    self.set_row_col(row , col , 0)

            #this means that the sudoku configuration is invalid 
            return False





if __name__ == "__main__":

    N = 9

    s = Board(N)
    s.print_sudoku_board()
    print("**********************************")

    solver = SudokuSolver(N)

    print("**********************************")

    solver.is_move_valid()
    print("**********************************")
    print("**********************************")
    print("**********************************")
    s.print_sudoku_board()
    print("**********************************")
    solver.print_sudoku_board()
    print("@@@@@@@@@@@@@@@@@@@@@")
    solver.get_sudoku_board()


