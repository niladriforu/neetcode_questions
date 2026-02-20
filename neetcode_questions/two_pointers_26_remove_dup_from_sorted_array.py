from typing import List
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         left = 1
#         for right in range(1, len(nums)):
#             if nums[left - 1] != nums[right]:
#                 nums[left] = nums[right]
#                 left += 1
#         return left
#
#

class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        return len(list(set(nums)))

if __name__ == "__main__":
    mylist = [0,0,1,1,1,2,2,3,3,4]
    sol = Solution1()
    print(sol.removeDuplicates(mylist))

