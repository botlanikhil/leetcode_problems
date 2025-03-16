class Solution(object):
    def generate(self, numRows):
        result = [[1]]  # First row is always [1]
        
        for i in range(1, numRows):  
            prev_row = result[-1]  # Get the previous row
            new_row = [1]  # First element is always 1
            
            for j in range(1, i):  # Compute the middle values
                new_row.append(prev_row[j - 1] + prev_row[j])
            
            new_row.append(1)  # Last element is always 1
            result.append(new_row)
        
        return result
