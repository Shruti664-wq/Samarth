#!/usr/bin/env python3
"""
Tic Tac Toe with an unbeatable AI (minimax).
Save as tictactoe_ai.py and run with: python3 tictactoe_ai.py
No dependencies outside the Python standard library.
"""

import math
import random

EMPTY = " "
HUMAN = None  # will be set based on user choice
AI = None


def print_board(board):
    # board is a list of 9 cells
    def cell(i):
        return board[i] if board[i] != EMPTY else str(i + 1)

    print()
    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")
    print()


def check_winner(board):
    win_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for a, b, c in win_lines:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    if EMPTY not in board:
        return "Draw"
    return None


def available_moves(board):
    return [i for i, v in enumerate(board) if v == EMPTY]


def minimax(board, player):
    """
    Returns a tuple (best_score, best_move_index)
    Scores: +1 -> AI win, -1 -> human win, 0 -> draw
    """
    winner = check_winner(board)
    if winner == AI:
        return 1, None
    elif winner == HUMAN:
        return -1, None
    elif winner == "Draw":
        return 0, None

    if player == AI:
        best_score = -math.inf
        best_move = None
        for m in available_moves(board):
            board[m] = AI
            score, _ = minimax(board, HUMAN)
            board[m] = EMPTY
            if score > best_score:
                best_score = score
                best_move = m
                # immediate win
                if best_score == 1:
                    break
        return best_score, best_move
    else:
        best_score = math.inf
        best_move = None
        for m in available_moves(board):
            board[m] = HUMAN
            score, _ = minimax(board, AI)
            board[m] = EMPTY
            if score < best_score:
                best_score = score
                best_move = m
                if best_score == -1:
                    break
        return best_score, best_move


def ai_move(board, difficulty="unbeatable"):
    # difficulty: "unbeatable" (minimax), "medium" (random with some strategy), "easy" (random)
    moves = available_moves(board)
    if difficulty == "easy":
        return random.choice(moves)
    elif difficulty == "medium":
        # select winning move if available, block if necessary, otherwise random
        # try winning
        for m in moves:
            board[m] = AI
            if check_winner(board) == AI:
                board[m] = EMPTY
                return m
            board[m] = EMPTY
        # try block
        for m in moves:
            board[m] = HUMAN
            if check_winner(board) == HUMAN:
                board[m] = EMPTY
                return m
            board[m] = EMPTY
        # play center if free
        if 4 in moves:
            return 4
        return random.choice(moves)
    else:
        _, move = minimax(board, AI)
        return move


def human_move(board):
    moves = available_moves(board)
    while True:
        try:
            choice = input(f"Your move ({', '.join(str(m + 1) for m in moves)}): ").strip()
            if choice.lower
