#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

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

def evaluate(board):
    winner = check_winner(board)
    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing):
    if check_winner(board):
        return evaluate(board)

    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    score = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                score = minimax(board, 0, False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

def tic_tac_toe_ai():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe AI!")

    while True:
        print_board(board)
        player_row = int(input("Enter the row number (0, 1, 2): "))
        player_col = int(input("Enter the column number (0, 1, 2): "))

        if board[player_row][player_col] != " ":
            print("That cell is already occupied. Try again.")
            continue

        board[player_row][player_col] = "O"

        if check_winner(board):
            print_board(board)
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "X"

        if check_winner(board):
            print_board(board)
            print("Sorry, the AI wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

tic_tac_toe_ai()


# In[ ]:




