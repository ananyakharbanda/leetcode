class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        slist = s.split(' ')
        if len(slist) != len(pattern):
            return False

        sdict = {}
        pdict = {}

        for i in range(len(slist)):
            if slist[i] not in sdict:
                sdict[slist[i]] = pattern[i]
            else:
                if sdict[slist[i]] != pattern[i]:
                    return False
            
            if pattern[i] not in pdict:
                pdict[pattern[i]] = slist[i]
            else:
                if pdict[pattern[i]] != slist[i]:
                    return False
        
        return True
