# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
from typing import List

#O(n2) solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for left in range(len(nums)):
            for right in range(left+1,min(len(nums),left+k+1)):
                if nums[left] == nums[right]:
                    return True
        return False
#O(n) solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        window = set()
        for right in range(len(nums)):
            if right - left + 1 > k+1:
                window.remove(nums[left])
                left+=1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False
