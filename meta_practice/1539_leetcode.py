from typing import List
# need to take a missing count variable . It will tell us for how long we need to continue the loop
# curr = 1 should be taken just to know whether we have all the numbers.
# i to loop through
def findKthPositive( arr: List[int], k: int) -> int:
    missing_count = 0
    i = 0
    curr = 1
    while missing_count < k :
        if i < len(arr) and arr[i] == curr:
            i+=1
        else:
            missing_count+=1
            if missing_count == k:
                return curr
        curr+=1
    return None

print(findKthPositive([2,3,4,7,11],1))