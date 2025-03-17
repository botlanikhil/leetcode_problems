class Solution(object):
    def largestLocal(self, grid):
        nRows, nCols = len(grid), len(grid[0])

        result = [[0] * (nCols - 2) for _ in range(nRows - 2)]

        def findLargest(row, col):
            best = grid[row][col]
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    best = max(best, grid[i][j])
            return best

        for row in range(nCols - 2):
            for col in range(nRows - 2):
                result[row][col] = findLargest(row, col)
        return result
        