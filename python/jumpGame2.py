class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        curr = 0
        maxJ = 0
        for i in range(len(nums) - 1):
            maxJ = max(maxJ, i + nums[i])
            if i == curr:
                jumps += 1
                curr = maxJ
        return jumps
