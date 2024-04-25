import re

def sudoku_solution(filename):
    sudoku_list = []
    try:
        with open(filename) as file:
            for line in file:
                line_list = []
                line = line.strip()
                if re.findall("[0-9]{9}", line):
                    for num in line:
                        line_list.append(num)
                    sudoku_list.append(line_list)
                else:
                    return None
            return sudoku_list
    except FileNotFoundError:
        return None
    
def print_board(board, row = -1, column = -1):
    row_counter = 0
    for values in board:
        for i in range(0, 3):
            if row_counter == row and i == column:
                print("\033[31m", "[", values[i], "]", "\033[37m", end="", sep = "")
            else:
                print("[", values[i], "]", end="", sep = "")
        print(" ", end=" ")
        for j in range(3, 6):
            if row_counter == row and j == column:
                print("\033[31m", "[", values[j], "]", "\033[37m", end="", sep = "")
            else:
                print("[", values[j], "]", end="", sep = "")
        print(" ", end=" ")
        for k in range(6, 9):
            if row_counter == row and k == column:
                print("\033[31m", "[", values[k], "]", "\033[37m", end="", sep = "")
            else:
                print("[", values[k], "]", end="", sep = "")
        print("\n", end="")
        row_counter += 1
        if row_counter == 9:
            ...
        elif row_counter % 3 == 0:
            print("\n", end="")

def validate_sudoku(board):
    for i in range(0, 9): #validating rows
        row_set = set()
        for j in range(0, 9):
            num = int(board[i][j])
            if num < 1 or num > 9 or num in row_set: 
                print_board(board, i, j)
                return False
            row_set.add(num)

    for j in range(0, 9): #validating columns
        col_set = set()
        for i in range(0, 9):
            num = int(board[i][j])
            if num < 1 or num > 9 or num in col_set: 
                print_board(board, i, j)
                return False
            col_set.add(num)
    
    #validating 3x3 squares
    valid, i, j = square_check(board, range(0, 3), range(0, 3))
    if valid == False:
        print_board(board, i, j)
        return False
    valid, i, j = square_check(board, range(0, 3), range(3, 6))
    if valid == False:
        print_board(board, i, j)
        return False
    valid, i, j = square_check(board, range(0, 3), range(6, 9))
    if valid == False:
        print_board(board, i, j)
        return False
    valid, i, j = square_check(board, range(3, 6), range(0, 3))
    if valid == False:
        print_board(board, i, j)
        return False
    valid, i, j = square_check(board, range(3, 6), range(3, 6))
    if valid == False:
        print_board(board, i, j)
        return False
    valid, i, j = square_check(board, range(3, 6), range(6, 9))
    if valid == False:
        print_board(board, i, j)
        return False
    valid, i, j = square_check(board, range(6, 9), range(0, 3))
    if valid == False:
        print_board(board, i, j)
        return False
    valid, i, j = square_check(board, range(6, 9), range(3, 6))
    if valid == False:
        print_board(board, i, j)
        return False
    valid, i, j = square_check(board, range(6, 9), range(6, 9))
    if valid == False:
        print_board(board, i, j)
        return False
    
    return True #if every test is valid
        

def square_check(board, rows, columns): #checks the 3x3 squares
    row_set = set()
    for i in rows:
        for j in columns:
            num = int(board[i][j])
            if num < 1 or num > 9 or num in row_set:
                #print(i, j)   test code
                return False, i, j
            row_set.add(num)
    return True, -1, -1

def main():
    sudoku_data = ["data/sud/invalid_001.sud", "data/sud/invalid_002.sud", "data/sud/invalid_003.sud", "data/sud/invalid_004.sud", "data/sud/invalid_005.sud", "data/sud/valid_001.sud", "data/sud/valid_002.sud", "data/sud/valid_003.sud", "data/sud/valid_004.sud", "data/sud/valid_005.sud", "data/sud/valid_006.sud", "data/sud/valid_007.sud", "data/sud/valid_008.sud", "data/sud/valid_009.sud", "data/sud/valid_010.sud"]
    for data in sudoku_data:
        print(data)
        board = sudoku_solution(data)
        if validate_sudoku(board) == True:
            print("This solution is valid")
        else:
            print("This solution is invalid")
        print()
    
if __name__ == "__main__":
    main()