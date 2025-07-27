class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=''
        s=s.lower()
        for i in s:
            if i.isalnum():
                c+=i
        return  c==c[::-1]
        

        