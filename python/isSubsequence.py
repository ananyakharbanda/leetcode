class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tsub = ''
        idx = 0
        for c in s:
            while idx < len(t) and t[idx] != c:
                idx += 1
            if idx == len(t):  
                return False
            tsub += c
            idx += 1  

        return True  
