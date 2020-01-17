def factorial(n):
    '''
    Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).
    '''

    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input())
print(factorial(n))