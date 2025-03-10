class Solution(object):
    def isSubsequence(self, s, t):
        s_index = 0  
        t_index = 0 
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:  
                s_index += 1
            t_index += 1        
        return s_index == len(s) 

