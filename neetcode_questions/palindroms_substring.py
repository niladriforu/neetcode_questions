class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for seq, num in enumerate(nums):
            if seq > 0 and nums[seq] == nums[seq - 1]:
                continue

            left, right = seq + 1, len(nums) - 1
            while left < right:
                threesum = num + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res


