class Solution(object):
    def removeStars(self, s):
        n = len(s)
        stack = []
        
        for i in range(n):
            if s[i] != '*':
                stack.append(s[i])
            else:
                stack.pop()
                
        return "".join(stack) 
        