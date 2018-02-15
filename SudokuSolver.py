# this program will solve a 9x9 Sudoku Puzzle given to it

sudoku_puzzle = []


# 0 means not used, 1 means used
# will read user input
def read_input():
    print("Please input the puzzle")
    puzzle = []
    for i in range(9):
        puzzle.insert(i, input())
    return puzzle


# declaring what main function is
def main():
    sudoku = (read_input())

    puzzle = []
    for i in range(9):
        puzzle.extend([int(i) for i in sudoku[i].split()])

    global sudoku_puzzle
    sudoku_puzzle = puzzle

    check = 0
    for i in range(81):
        check += check_board(i, puzzle)
    if check != 81:  # 243 = 81*1, since checking 81 times
        print("Bad board given.")
        return  # end of program

    solved = 0

    if check == 81:  # if input valid, continue with the code
        solved = solve_sudoku(0)
    if solved == 1:
        print("Solved.")
    else:
        print("No solution.")


def print_sudoku(puzzle):
    for i in range(81):
        if i % 9 == 0:
            print()
        print(puzzle[i], end=' ')
    print("\n")


def solve_sudoku(location):

    global sudoku_puzzle

    correct = 0

    if location == 81:
        print_sudoku(sudoku_puzzle)
        return 1  # 1 indicates we solved the puzzle

    if sudoku_puzzle[location] != 0:  # indicates there's already another number here
        return solve_sudoku(location+1)

    for i in range(1, 10):  # go through all 10 possibilities in each slot
        sudoku_puzzle[location] = i
        if check_board(location, sudoku_puzzle) == 1:
            correct += solve_sudoku(location+1)
        sudoku_puzzle[location] = 0
        if correct >= 1:
            return correct

    return correct


# checks if board given is valid
def check_board(location, puzzle):

    ret_val = 0
    ret_val += check_row(location, puzzle)
    ret_val += check_column(location, puzzle)
    ret_val += check_box(location, puzzle)

    if ret_val != 3:
        return 0  # board was not correct
    return 1  # board is fine


# checks if there are any duplicates in current column
def check_column(location, puzzle):
    frequency = []

    for i in range(10):
        frequency.append(0)

    i = location % 9  # finding what column we are in
    while i < 81:
        frequency[puzzle[i]] += 1
        i += 9  # go down 1 in the column

    for i in range(1, 10):
        if frequency[i] > 1:
            return 0  # 0 means column is not correct
    return 1  # column had no duplicates


# checks if there are any duplicates in current row
def check_row(location, puzzle):
    frequency = []
    frequency.clear()
    for i in range(10):
        frequency.append(0)

    location //= 9  # finding what row we are in
    location *= 9
    for i in range(location, (location+9)):
        frequency[puzzle[i]] += 1

    for i in range(1, 10):
        if frequency[i] > 1:
            return 0  # row is not correct
    return 1  # no duplicates in this row


def check_box(location, puzzle):
    frequency = []

    for i in range(10):
        frequency.append(0)
    # finding what column 3x3 box is in
    col = location // 3
    col %= 3
    col *= 3

    # what row 3x3 box is in
    row = location // 27
    row *= 27

    # first slot of 3x3 box
    slot = row + col
    next_row = 0
    for i in range(9):
        if next_row > 0 and next_row % 3 == 0:
            slot += 6
        frequency[puzzle[slot]] += 1
        slot += 1
        next_row += 1

    # checking for duplicates
    for i in range(1, 10):
        if frequency[i] > 1:
            return 0  # 3x3 box is incorrect
    return 1  # 3x3 box is correct


# launching main function
if __name__ == '__main__':
    main()
