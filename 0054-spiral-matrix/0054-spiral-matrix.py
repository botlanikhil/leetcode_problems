class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        l = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse top row
            for j in range(left, right + 1):
                l.append(matrix[top][j])
            top += 1

            # Traverse right column
            for i in range(top, bottom + 1):
                l.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Traverse bottom row
                for j in range(right, left - 1, -1):
                    l.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                # Traverse left column
                for i in range(bottom, top - 1, -1):
                    l.append(matrix[i][left])
                left += 1

        return l
            