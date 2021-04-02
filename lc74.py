class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # the sorted case, consider dichotomy
        # --- FLOW ---
        # 1. we init a 2D pointers [0, 0] & [m-1, n-1],
        #   1.1 search criterion: l[0] < r[0] or l[0] == r[0] and l[1] <= r[1] 
        # 2. each time, we first check if target on the line
        #   2.1 we first loc the row index[i_0]
        #   2.2 we then loc the nums index[i_0][j_0] in i_0 - th row
        # --- init ---
        m, n = len(matrix), len(matrix[0])
        l, r = [0, 0], [m-1, n-1]

        # --- locate row ---
        row = None
        while l[0] <= r[0]:
            mid = (l[0] + r[0]) // 2
            if mid == l[0] or mid == r[0]:
                if matrix[l[0]][0] <= target <= matrix[l[0]][n-1]:
                    row = l[0]
                    break
                elif matrix[r[0]][0] <= target <= matrix[r[0]][n-1]:
                    row = r[0]
                    break
                else:
                    return False 
            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                row = mid
                break
            if matrix[mid][0] > target:
                r[0] = mid
            if matrix[mid][n-1] < target:
                l[0] = mid
        if row is None:
            return False
        
        # --- locate colume ---
        while l[1] <= r[1]:
            mid = (l[1] + r[1]) // 2
            if mid == l[1] or mid == r[1]:
                if matrix[row][l[1]] == target:
                    return True
                elif matrix[row][r[1]] == target:
                    return True
                else:
                    return False
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                l[1] = mid
            if matrix[row][mid] > target:
                r[1] = mid