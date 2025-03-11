class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        indexMap = {}
        i = 0  
        for num in nums:
            if num in indexMap and i - indexMap[num] <= k:
                return True
            indexMap[num] = i  
            i += 1  
        return False
