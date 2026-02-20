class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for right in range(len(nums)):
            counterpart = target - nums[right]
            if counterpart in seen:
                return [seen[counterpart],right]
            else:
                seen[nums[right]] = right
        return []

