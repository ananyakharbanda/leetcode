class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        curr_sum = 0
        min_length = None
    
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_length = min(right - left + 1, min_length)
                curr_sum -= nums[left]
                left += 1
        return min_length
