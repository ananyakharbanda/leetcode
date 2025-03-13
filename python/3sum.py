class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        trips = []
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                elif total == 0:
                    if [nums[i], nums[left], nums[right]] not in trips:
                        trips.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        return trips
