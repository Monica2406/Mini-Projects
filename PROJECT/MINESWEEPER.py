#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
def create_board(rows, cols, num_mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mines_placed = 0
    while mines_placed < num_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if board[row][col] != '*':
            board[row][col] = '*'
            mines_placed += 1
    for r in range(rows):
        for c in range(cols):
            if board[r][c] != '*':
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if 0 <= r + dr < rows and 0 <= c + dc < cols and board[r + dr][c + dc] == '*':
                            count += 1
                board[r][c] = str(count) if count > 0 else ' '

    return board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * (4 * len(row) - 1))
def reveal_board(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == '*':
                board[r][c] = '*'
def play_game(rows, cols, num_mines):
    board = create_board(rows, cols, num_mines)
    print("Welcome to Minesweeper!")
    print_board(board)
    while True:
        row = int(input("Enter row number: "))
        col = int(input("Enter column number: "))
        if board[row][col] == '*':
            print_board(board)
            print("Game over! You hit a mine.")
            reveal_board(board)
            print_board(board)
            break
        elif board[row][col] != ' ':
            print("Cell already revealed. Try another one.")
        else:
            reveal_cells(board, row, col)
            print_board(board)
            if check_win(board):
                print("Congratulations! You've cleared all safe cells.")
                break
def reveal_cells(board, row, col):
    if board[row][col] != ' ':
        return
    board[row][col] = '0'
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if 0 <= row + dr < len(board) and 0 <= col + dc < len(board[0]):
                reveal_cells(board, row + dr, col + dc)
def check_win(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True
play_game(5, 5, 5)  


# In[ ]:




