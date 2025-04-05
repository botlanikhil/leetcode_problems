class Solution(object):
    def generateMatrix(self, n):
        c = 1
        mat = [[0 for _ in range(n)] for _ in range(n)]

        '''for i in range(n):
            for j in range(n):
                mat[i][j] = c
                c += 1
                if not mat:
                    return []'''
        top, bottom = 0,n- 1
        left, right = 0,n- 1

        while top <= bottom and left <= right:
        # Left to Right
            for j in range(left, right + 1):
                mat[top][j] = c
                c += 1
            top += 1

            # Top to Bottom
            for i in range(top, bottom + 1):
                mat[i][right] = c
                c += 1
            right -= 1

            # Right to Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    mat[bottom][j] = c
                    c += 1
                bottom -= 1

            # Bottom to Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    mat[i][left] = c
                    c += 1
                left += 1

        return mat