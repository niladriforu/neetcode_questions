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


if __name__ == '__main__':
    mylist = [ 1,2,2,5,3,5]
    window_size = 3
    print(closeDupplicatesBruteForce(mylist,window_size))
    # closeDupplicatesBruteForce(mylist,window_size)
