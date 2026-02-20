from collections import defaultdict
import sys

word = sys.argv[1]
option = sys.argv[2]


vowels = 'aeiouAEIOU'
mydict = defaultdict(int)

if option.lower() == 'vowel':
    for char in word:
        if char in vowels:
            mydict[char.lower()] += 1
        else:
            continue

    print(dict(mydict))
elif option.lower() == 'total':
    print(sum(1 for char in word if char in vowels))

#upper case letters have lower ASCII than lower case letters.
