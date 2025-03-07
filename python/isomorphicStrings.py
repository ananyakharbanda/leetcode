class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        sdict = {}
        tdict = {}
        
        for i in range(len(s)):
            if s[i] not in sdict:
                sdict[s[i]] = t[i]
            else:
                if sdict[s[i]] != t[i]:
                    return False
            
            if t[i] not in tdict:
                tdict[t[i]] = s[i]
            else:
                if tdict[t[i]] != s[i]:
                    return False
        
        return True
