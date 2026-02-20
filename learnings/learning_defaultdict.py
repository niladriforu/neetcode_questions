# There is a pattern in assigning values to a defaultdict.
# Defaultdict is not a regular dict that sets default values to a dict.
# The nature of using the defaultdict is totally different that using a dict
# If we assign values like a regular dict, it will lose defaultdict property and become a dict.

from collections import defaultdict

mydict = defaultdict(int)

mydict["a"] # will give you value 0. The type of mydict is defaultdict()
mydict["b"] # will give you value 0. The type of mydict is defaultdict()
mydict["c"] = 2
mydict["c"] # will give you value 2.

mydict = {"d" : 3} # This will give value as 3 , but it will wipe of any other values with keys a, b,c and
                   # will convert the defaultdict mydict to a normal dict.
