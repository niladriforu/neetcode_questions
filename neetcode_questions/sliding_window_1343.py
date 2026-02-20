import statistics as s
from typing import List

# This worked with run but failed with submit citing
#statistics.StatisticsError: mean requires at least one data point

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        count = 0
        avg_threshold = 0
        for right in range(len(arr)):
            if right - left == k -1:
                left+=1
                avg_threshold = s.mean(arr[left:right+1])
                if avg_threshold >=threshold:
                    count+=1
        return count if count > 0 else 0

# This worked after submit.

import statistics as s
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        count = 0
        array_sum = 0
        avg_threshold = 0
        for right in range(len(arr)):
            array_sum+=arr[right]
            if right - left >= k -1:
                left+=1
                avg_threshold = array_sum/k
                if avg_threshold >=threshold:
                    count+=1
                array_sum-=arr[right - k + 1]
        return count if count > 0 else 0


