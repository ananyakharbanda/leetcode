class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        output = []
        i = 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j + 1] - nums[j] == 1:
                j += 1
            if i == j:
                output.append(str(nums[i]))
            else:
                output.append("{}->{}".format(nums[i], nums[j]))
            i = j + 1  
        return output
