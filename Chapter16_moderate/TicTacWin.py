'''
Design an algorithm to figure out if someone has won a game of tic-tac-toe.
Extend it to NxN
'''

class matrix:
  def __init__(self, M):
    self.rows = M[0 : len(M[0])]
    self.cols = [[M[i][j] for i in range(len(M[0]))] for j in range(len(M))] 
    self.diag = [[M[i][i] for i in range(len(M))], [M[j][len(M[0])-1-j] for j in range(len(M))]]

def line_win(line):
  if line[0] == '': 
    return False
  i = 0
  while i < len(line) - 1:
    if line[i] != line[i + 1]:
      return False
    i += 1
  return True

def last_col_win(M, n):
  return line_win(M.cols[n])

def last_row_win(M, n):
  return line_win(M.rows[n])

def princ_diag_win(M):
  return line_win(M.diag[0])

def last_diag_win(M):
  return line_win(M.diag[1])

def tt_win(M, n, w):

  if n < 0:
    return w

  w = tt_win(M, n - 1, w) 
  
  for el in w:
    if el[n-1] != el[n]:
      w.remove(el)
  
  if last_col_win(M, n):
    w.append(M.cols[n])
  if last_row_win(M, n):
    w.append(M.rows[n])

  return w

def tic_tac_win(M):
  
  win_lines = []
  win_lines = tt_win(M, len(M.rows) - 1, win_lines)

  if princ_diag_win(M):
    win_lines.append(M.diag[0])
  if last_diag_win(M):
    win_lines.append(M.diag[1])

  return win_lines    
  
tic_tac_matrix = [
  ['X', 'X', 'O', 'X'],
  ['O', '', 'X', 'X'],
  ['X', 'X', '', 'X'],
  ['X', 'X', 'O', 'X']]

test_M = matrix(tic_tac_matrix)
print(tic_tac_win(test_M))



