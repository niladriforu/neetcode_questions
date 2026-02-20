from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        right_nums1 = m-1
        right_nums2 = n-1
        end_nums1 = m+n-1
        # I am looping on the index
        for z in range(end_nums1,-1,-1):
            if right_nums1 < 0:
                nums1[end_nums1] = nums2[right_nums2]
                right_nums2-=1
                end_nums1-=1
            elif right_nums2 < 0 :
                break
            elif nums1[right_nums1] <= nums2[right_nums2]:
                    nums1[end_nums1]=nums2[right_nums2]
                    right_nums2-=1
                    end_nums1-=1
            elif nums2[right_nums2] < nums1[right_nums1]:
                    nums1[end_nums1] = nums1[right_nums1]
                    right_nums1-=1
                    end_nums1-=1
        return nums1

s = Solution()
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
print(s.merge(nums1,m,nums2,n))



