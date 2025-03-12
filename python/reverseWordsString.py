class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        stripped = s.strip()  
        slist = stripped.split()  
        slist.reverse()  
        return ' '.join(slist) 