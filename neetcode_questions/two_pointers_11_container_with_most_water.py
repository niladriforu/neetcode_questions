#The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. Further, the farther the lines, the more will be the area obtained.

class Solution:
    def maxArea(self, height: List[int]) -> int:
            left = 0
            right = len(height) -1
            max_area = 0
            while left < right:
                min_height = min(height[left],height[right])
                width = right - left
                max_area = max(max_area, width * min_height)
                # This is because the lower of left and right will start to hold water.
                # That means if the left is lower, we increment left to see whether the next iteration can also contain water
                # if the right is lower, we decrease right .
                if height[left] <= height[right]:
                    left+=1
                else:
                    right-=1
            return max_area
