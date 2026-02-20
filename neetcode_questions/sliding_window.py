def closeDupplicatesBruteForce(mylist, size):
    '''
    This function takes a list and a window size and checks if there are any duplicates in the window
    Alternatively,this can be also adjacent two numbers in the list that are equal #for right in range(left+1, min(len(mylist),left+size))
    Alternatively,this can be also two alternate numbers in the list that are equal #for right in range(left+2, min(len(mylist),left+size+1))
    :param mylist:
    :param size:
    :return:
    '''
    for left in range(len(mylist)):
            print(f'left is {left}')
            # for right in range(left+2, min(len(mylist),left+size+1)) :
            for right in range(left+1, min(len(mylist),left+size)) :
                # It actually means that the window is from left to left+size
                # and we are taking the first element of the window and checking
                # if the other elements in the window are same.
                # This also means the mylist[left+size] element is not compared.
                # only the elements in the window are compared.
                print(f'range is  : {left} "::"  {left+size}')
                print('00000000000')
                if mylist[left] == mylist[right]:
                    print(f'found a duplicate at {left} and {right}')
                    return True
    return False


def closeDuplicates(mylist,size):
    window = set()
    left = 0
    for right in range(len(mylist)):
        if right - left +1 > size:
            window.remove(mylist[left])
            left +=1
        if mylist[right] in window:
            return True
        window.add(mylist[right])
    return False


def longestSubarrayWithSameValue(mylist):
    left = 0
    size = 0 # window size
    for right in range(len(mylist)):
        # for first iteration , this will be false.
        # hence it will go directly to calculate the window size
        # from second iteration, if the adjacent numbers match, it will continue increasing the windo
        # That happens here by calculating the max window size
        if mylist[right] != mylist[left]:
            left = right
        size = max(size,right - left + 1)
    return size





if __name__ == '__main__':
    # This is for questions where we need to see if there is a duplicate number in a window of N
    mylist = [ 1,2,3,5,4,6]
    window_size = 3
    # print(closeDupplicatesBruteForce(mylist,window_size))
    # print(closeDuplicates(mylist,window_size))

    # This is for questions where we need to find out the longest subarray with same value at each position :
    mylist = [ 4,2,3,7,3,8]
    print(longestSubarrayWithSameValue(mylist))
    # This is for questions where we need to find out the longest subarray without same value at each position :

    # This is for questions where we need to find out the longest substring without repeating characters

    # This is for questions where we need to find out the longest substring with repeating characters


    # We have an array and a sliding window defined by a start index and an end index.
    # The sliding window moves from left of the array to right. There are always k elements in the window.
    # The window moves one position at a time. Find the maximum integer within the window each time it moves.


