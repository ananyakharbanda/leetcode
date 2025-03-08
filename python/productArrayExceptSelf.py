class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1] * n  
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix = prefix * nums[i]
        
        suffix = 1
        for j in range(n - 1, -1, -1):
            output[j] = output[j] * suffix
            suffix = suffix * nums[j]

        return output
