"""
Conway's Game of Life
Imagine a grid where you randomly place cells and then observe 
how they grow according to the rules:

Cell with less than 2 neighbors dies
Cell with more than 3 neighbors dies
Empty space with exactly 3 neighbors comes to life as a new cell
"""

# python -m doctest

import random
import time

EMPTY = 0  
ALIVE = 1

board = [
  [EMPTY, ALIVE, EMPTY],
  [EMPTY, ALIVE, EMPTY],
  [EMPTY, ALIVE, EMPTY]
]

def nothing_serious():
  print(board)
  print(board[0][0])

nothing_serious()







def prepare_new_board(w=15, h=15, randomly=True):
  """
  Create a new board filled with random values
  >>> init_board(2, 2, randomly=False)
  [[0, 0], [0, 0]]
  >>> init_board(3, 3, randomly=False)
  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  """
  board = []
  return board

def display_board(board):
  board_text = get_board_text(board)
  print(board_text)

def update_board(board):
  """
  updates all cells based on GOL rules
  tests:
  >>> update_board([[EMPTY, EMPTY], [EMPTY, EMPTY]])
  [[0, 0], [0, 0]]
  >>> update_board([[ALIVE, ALIVE], [ALIVE, ALIVE]])
  [[1, 1], [1, 1]]
  >>> update_board([[ALIVE, ALIVE, ALIVE], [ALIVE, ALIVE, ALIVE], [ALIVE, ALIVE, ALIVE]])
  [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
  """
  board = []
  return board

def neighbours_count(board, rowNo, cellNo):
  """
  >>> neighbours_count([\
                        [EMPTY, EMPTY, EMPTY],\
                        [EMPTY, EMPTY, EMPTY],\
                        [EMPTY, EMPTY, EMPTY]], 1, 1)
  0
  >>> neighbours_count([\
                        [EMPTY, ALIVE, EMPTY],\
                        [EMPTY, EMPTY, EMPTY],\
                        [EMPTY, EMPTY, EMPTY]], 1, 1)
  1
  >>> neighbours_count([\
                        [ALIVE, ALIVE, ALIVE],\
                        [ALIVE, EMPTY, ALIVE],\
                        [ALIVE, ALIVE, ALIVE]], 1, 1)
  8
  >>> neighbours_count([\
                        [EMPTY, ALIVE, ALIVE],\
                        [ALIVE, ALIVE, ALIVE],\
                        [ALIVE, ALIVE, ALIVE]], 0, 0)
  3
  >>> neighbours_count([\
                        [ALIVE, ALIVE, ALIVE],\
                        [ALIVE, ALIVE, ALIVE],\
                        [ALIVE, ALIVE, EMPTY]], 2, 2)
  3
  """
  sum_of_neighbours = -1
  return sum_of_neighbours

def get_board_text(board):
  """
  transforms a board into text which can be displayed
  >>> get_board_text([[EMPTY, EMPTY],[EMPTY, EMPTY]])
  '  \\n  \\n'
  """
  LABELS = {0 :  ' ', 1 : '#' }
  board_text = ''
  return board_text

def main():
  board = []
  prepare_new_board(board)
  while True:
    display_board(board)
    update_board(board)
    time.sleep(0.5)


if __name__ == '__main__':
  main()