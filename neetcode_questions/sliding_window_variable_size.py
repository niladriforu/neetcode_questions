# Find the length of longest subarray with the same
# value in each position: O(n)
def longestSubArray(nums):
    length = 0
    left = 0
    for right in range(len(nums)):
        if nums[right] != nums[left]:
            right = left
            length = max(length,right - left + 1)
        return length

# Find length of the minimum size subarray where the sum is
# greater than or equal to the target.
# Assume all values in the input are positive.
# O(n)

def shortestSubArray(nums, target):
     left = 0
     total = 0
     length = float("inf")
     for right in range(len(nums)):
         total+=nums[right]
         while total >= target:
             length = min(right - left + 1,length)
             total-=nums[left]
             left+=1
     return 0 if length==float("inf") else length






