def factorial1(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

def factorial(n):
    stack = []
    while n > 0:
        stack.append(n)
        n-=1

    result = 1
    while stack:
        result *= stack.pop()











