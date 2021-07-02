"""
Conway's Game of Life (Google it)
   @
    @
  @@@

Imagine a grid where you randomly place cells.
How they grow according to the rules:

  1. Cell with less than 2 neighbours dies
  2. Cell with more than 3 neighbours dies
  3. Empty space with exactly 3 neighbours becomes a new cell
"""

import random
import time

EMPTY = 0  
ALIVE = 1

board = [
  [EMPTY, ALIVE, EMPTY],
  [EMPTY, ALIVE, EMPTY],
  [EMPTY, ALIVE, EMPTY]
]

print(board)
print(board[0][0])
print(board[0][0] == ALIVE)
print(board[0][1] == ALIVE)


def prepare_new_board():
  pass

def display_board():
  pass

def update_board():
  pass


def main():
  board = prepare_new_board()
  while True:
    display_board(board)
    update_board(board)
    time.sleep(0.5)
    break # execute the loop only once (for testing only)


if __name__ == '__main__':
  main()
