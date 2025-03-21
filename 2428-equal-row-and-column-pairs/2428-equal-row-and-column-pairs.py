class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)
        hash = {}
        pairs = 0
        for i in range(n):
            row = tuple(grid[i])
            hash[row] = hash.get(row, 0) + 1     
        for j in range(n):
            column = tuple(grid[i][j] for i in range(n))
            if column in hash:
                pairs += hash[column]
        return pairs 
        