
def firstTenMultiples(n):
    '''
    Given an integer, n, print its first 10 multiples. Each multiple n*i (where 1<= i <= 10) should be printed 
    on a new line in the form: n x i = result.
    '''

    for i in range(10):
        res = n*(i+1)
        print(f"{n}x{i+1} = {res}")

n = int(input())
firstTenMultiples(n)