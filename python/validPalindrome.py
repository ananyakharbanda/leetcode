class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stripped = s.replace(' ', '')
        new = ''
        
        for a in stripped:
            if a.isalnum():
                new += a.lower()
        
        n = len(new)
        half = n // 2
        
        if n % 2 == 0:
            first = new[:half]
            second = new[half:]
        else:
            first = new[:half]
            second = new[half+1:]
        
        secondrev = second[::-1]
        
        if first == secondrev:
            return True
        else:
            return False
