from collections import Counter

arr = [ 1,2,1,3,1,6,1,2,9]

counter=Counter(arr)

print(counter) # will give a dictionary with maximum repeating elements

print(counter.most_common(1)[0][1]) # maximum value in that counter