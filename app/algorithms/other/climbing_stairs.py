def find_solutions(n: int):
    """ You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Solution: Uses Fibonacci series
    """


    if n == 1:
        return 1
    
    n_minus_2 = 1
    n_minus_1 = 2

    for i in range(3, n+1):
        current = n_minus_2 + n_minus_1
        n_minus_2 = n_minus_1
        n_minus_1 = current
    
    return n_minus_1
