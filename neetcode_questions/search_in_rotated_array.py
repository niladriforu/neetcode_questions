def search(nums,target) -> int:
    beg , end = 0 , len(nums)-1
    while beg < end :
        mid = ( beg + end ) //2

        if nums[mid] == target:
            return mid
        # At the first step, this condition will always be true . things will change once
        # we start playing with beg and end values
        if nums[beg] <=nums[mid]:
            if nums[beg] <=target <=nums[mid]:
                end = mid -1
            else:
                beg = mid + 1
        else:
            if nums[mid] <=target <=nums[end]:
                beg = mid +1
            else:
                end = mid - 1
        # this last line will contain the final value if it is not the mid value.
        # i.e. in any range, finally if we close in on one value ( beg and end are same )
        return -1 if nums[end] != target else end





p = search([4,5,6,7,1,2,3],30)
print(p)