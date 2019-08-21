# python -m doctest
import random
import time
import copy
from functools import reduce

DEAD = 0  
ALIVE = 1
LABEL = {0 :  ' ', 1 : '▮' }

def get_board_text(board):
  """
  >>> get_board_text([[DEAD, DEAD],[DEAD, DEAD]])
  '  \\n  \\n'
  """
  board_text = ''
  for row in board:
    board_text += ''.join([LABEL[cell] for cell in row]) + '\n'
  return board_text

def is_empty(board):
  """
  >>> is_empty([[0, 0], [0, 0]])
  True
  """
  return not sum(reduce(lambda x, y: x + y, board))


def display_board(board):
  board_text = get_board_text(board)
  print(board_text)

def update_board(board):
  """
  >>> update_board([[DEAD, DEAD], [DEAD, DEAD]])
  [[0, 0], [0, 0]]
  >>> update_board([[ALIVE, ALIVE], [ALIVE, ALIVE]])
  [[1, 1], [1, 1]]
  >>> update_board([[ALIVE, ALIVE, ALIVE], [ALIVE, ALIVE, ALIVE], [ALIVE, ALIVE, ALIVE]])
  [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
  """
  new_board = copy.deepcopy(board)
  for (rowNo, row) in enumerate(board):
    for (cellNo, cell) in enumerate(row):
      if neighbours_count(board, rowNo, cellNo) > 3:
        new_board[rowNo][cellNo] = DEAD
      if neighbours_count(board, rowNo, cellNo) < 2:
        new_board[rowNo][cellNo] = DEAD
      if neighbours_count(board, rowNo, cellNo) == 3:
        new_board[rowNo][cellNo] = ALIVE
  return new_board

def neighbours_count(board, rowNo, cellNo):
  """
  >>> neighbours_count([\
                        [DEAD, DEAD, DEAD],\
                        [DEAD, DEAD, DEAD],\
                        [DEAD, DEAD, DEAD]], 1, 1)
  0
  >>> neighbours_count([\
                        [DEAD, ALIVE, DEAD],\
                        [DEAD, DEAD, DEAD],\
                        [DEAD, DEAD, DEAD]], 1, 1)
  1
  >>> neighbours_count([\
                        [ALIVE, ALIVE, ALIVE],\
                        [ALIVE, DEAD, ALIVE],\
                        [ALIVE, ALIVE, ALIVE]], 1, 1)
  8
  >>> neighbours_count([\
                        [ALIVE, ALIVE, ALIVE],\
                        [ALIVE, ALIVE, ALIVE],\
                        [ALIVE, ALIVE, ALIVE]], 0, 0)
  3
  >>> neighbours_count([\
                        [ALIVE, ALIVE, ALIVE],\
                        [ALIVE, ALIVE, ALIVE],\
                        [ALIVE, ALIVE, ALIVE]], 2, 2)
  3
  """
  sum = 0
  if rowNo > 0:
    sum += board[rowNo-1][cellNo] # top
  
  if rowNo < len(board) - 1: # ilosc wierszy
    sum += board[rowNo+1][cellNo] # bottom

  if cellNo > 0:
    sum += board[rowNo][cellNo - 1] # left
  
  if cellNo < len(board[rowNo]) - 1: 
    sum += board[rowNo][cellNo + 1] # right

  if rowNo > 0 and cellNo > 0:
    sum += board[rowNo - 1][cellNo - 1] # top left
  
  if rowNo < len(board) - 1 and cellNo < len(board[rowNo]) - 1: 
    sum += board[rowNo + 1][cellNo + 1] # bottom right
  
  if rowNo > 0 and cellNo < len(board[rowNo]) - 1:
    sum += board[rowNo - 1][cellNo + 1] # Top right
  
  if rowNo < len(board) - 1 and cellNo > 0:
    sum += board[rowNo + 1][cellNo - 1] # bottom left
  
  return sum


def init_board(board, w=15, h=15, randomly=True):
  """
  >>> init_board([], 2, 2, randomly=False)
  [[0, 0], [0, 0]]
  """

  for i in range(h):
    board.append([])
    for j in range(w):
      if randomly:
        cell_value = random.choice([DEAD, ALIVE])
      else:
        cell_value = DEAD
      board[i].append(cell_value)
  return board


def main():
  board = []
  init_board(board)
  while not is_empty(board):
    display_board(board)
    board = update_board(board)
    time.sleep(0.1)

if __name__ == '__main__':
  main()