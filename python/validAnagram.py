class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        sdict = {}
        tdict = {}

        for i in s:
            if i not in sdict:
                sdict[i] = 1
            else:
                sdict[i] += 1
        
        for i in t:
            if i not in tdict:
                tdict[i] = 1
            else:
                tdict[i] += 1
        
        if sdict == tdict:
            return True
        return False