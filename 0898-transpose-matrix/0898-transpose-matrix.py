class Solution(object):
    def transpose(self, matrix):
        result=[[0]*len(matrix) for i in range(len(matrix[0]))]
        for i in range(0,len(result)):
            for j in range(0,len(result[0])):
                result[i][j]=matrix[j][i]
        return result
        