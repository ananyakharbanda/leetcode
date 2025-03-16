class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        maxLen = 0
        subs = []
        for right in range(len(s)):  
            while s[right] in subs:  
                subs.pop(0)
                left += 1
            subs.append(s[right])  
            maxLen = max(maxLen, len(subs)) 
        return maxLen