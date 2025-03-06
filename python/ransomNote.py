class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
    
        charCount = {}
        for char in magazine:
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1
        
        for rans in ransomNote:
            if rans not in charCount or charCount[rans] == 0:
                return False
            else:
                charCount[rans] -= 1
        return True