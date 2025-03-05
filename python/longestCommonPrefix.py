class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]

        for word in strs[1:]:
            if len(prefix) < len(word):
                n = len(prefix)
            else:
                n = len(word)
            while prefix[:n] != word[:n]:
                n -= 1
                if n == 0:
                    return ''
            prefix = prefix[:n]  
        
        return prefix