def sell(arr):
    """ Say you have an array prices for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. 
    You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

    Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

    """


    buy = False
    amount = None
    profit = 0

    for i in range(1, len(arr)):
        if not buy and arr[i] > arr[i-1]:
            amount = arr[i-1]
            buy = True
        elif buy and arr[i] < arr[i-1]:
            profit = profit + arr[i-1] - amount
            buy = False
        elif buy and i == len(arr)-1 and arr[i] > amount:
            profit = profit + arr[i] - amount
    
    return profit
        