class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastI = 0
        for i in range(len(nums)):
            if i > lastI:
                return False
            lastI = max(i + nums[i], lastI)

            if lastI >= len(nums) - 1:
                return True        