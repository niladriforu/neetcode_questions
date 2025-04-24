'''
Get factorial
'''

def factorial(n):
    if n<1:
        return 1
    return n * factorial(n-1)

print(factorial(3))


def factorial1(n):
    stack = []
    while n > 0:
        stack.append(n)
        n-=1
    result =1
    while stack:
        p = stack.pop()
        result = result * p
    return result

print(factorial1(3))