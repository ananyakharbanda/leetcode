class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        appears = {}
        for i in nums:
            if i not in appears:
                appears[i] = 1
            else:
                appears[i] += 1
        
        for num in appears:
            if appears[num] > len(nums) / 2:
                return num

