def closeDupplicatesBruteForce(mylist, size):
    for left in range(len(mylist)-1):
            print(f'left is {left}')
            for right in range(left+1, left+size) :
                # It actually means that the window is from left to left+size
                # and we are taking the first element of the window and checking
                # if the other elements in the window are same
                if len(mylist) >=  left+size:
                    print(f'range is  : {left} "::"  {left+size}')
                    print('00000000000')
                    if mylist[left] == mylist[right]:
                        print(f'found a duplicate at {left} and {right}')
                        return True
    return False


if __name__ == '__main__':
    mylist = [ 1,2,3,2,23,4]
    window_size = 2
    print(closeDupplicatesBruteForce(mylist,window_size))
    # closeDupplicatesBruteForce(mylist,window_size)
