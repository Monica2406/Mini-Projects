#!/usr/bin/env python
# coding: utf-8

# In[2]:


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row number (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter the column number (0, 1, 2): "))

        if board[row][col] != " ":
            print("That cell is already occupied. Try again.")
            continue

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Congratulations! Player {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()


# In[ ]:




