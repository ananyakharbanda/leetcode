class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        listk = []
        for i in range(len(nums)):
            if nums[i] not in listk:
                listk.append(nums[i])
                nums[k] = nums[i]
                k += 1
        return k
