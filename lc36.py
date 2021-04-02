import copy

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ref = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, 
                '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

        # horizon / vertical check
        for i in range(9):
            v_ref = copy.copy(ref)
            h_ref = copy.copy(ref)
            for j in range(9):
                v = board[i][j]
                h = board[j][i]
                if v != '.':
                    v_ref[v] += 1
                    if v_ref[v] > 1:
                        return False
                if h != '.':
                    h_ref[h] += 1
                    if h_ref[h] > 1:
                        return False
        
        # 3 x 3 sliding windows check
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                w_ref = copy.copy(ref)
                for k in range(3):
                    for l in range(3):
                        w = board[i+k][j+l]
                        if w != '.':
                            w_ref[w] += 1
                            if w_ref[w] > 1:
                                return False
        return True 
            

import copy

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ref = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, 
                '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

        # horizon / vertical check
        for i in range(9):
            v_ref = copy.copy(ref)
            h_ref = copy.copy(ref)
            w_ref = copy.copy(ref)
            for j in range(9):
                v = board[i][j]
                h = board[j][i]
                if v != '.':
                    v_ref[v] += 1
                    if v_ref[v] > 1:
                        return False
                if h != '.':
                    h_ref[h] += 1
                    if h_ref[h] > 1:
                        return False

                # i-th sub-board
                w = board[(i % 3) * 3 + j // 3][(i // 3) * 3 + j % 3]
                if w != '.':
                    w_ref[w] += 1
                    if w_ref[w] > 1:
                        return False
        return True 


"""
Note:

In most cases, we treat i, j in [0, m-1], [0, n-1] as the index of rows / columes of a matrix / 2D - list
However, we can transform them to get a brand new traversary of a matrix. Actually, we can view the i as dividing
the matrix into 9 parts with a same shape. the basic element is a row? ok. a colume? ok. Even if a SUB-SQUARE is OK!
"""