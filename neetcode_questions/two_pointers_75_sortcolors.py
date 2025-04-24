class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(1,len(nums)):
            if nums[left] > nums[right]:
                nums[right] = nums[left]
                nums[left] = nums[right]
            elif nums[left] <= nums[right]:
                left+=1
        return nums




s = Solution()
nums = [2,0,2,1,1,0]
print(s.sortColors(nums))