class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1 = 2
        for pointer in range(2, len(nums)):
            if nums[pointer] != nums[p1-2]:
                nums[p1] = nums[pointer]
                p1 += 1
        return p1
            
