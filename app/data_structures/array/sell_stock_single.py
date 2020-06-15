def sell(prices):
    """ Say you have an array prices for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. 
    You may complete only one transaction that will give the maximum profit.

    """


    buy_price = None
    max_profit = 0

    for i in range(0, len(prices)):
        if buy_price is None:
            buy_price = prices[i]
        if prices[i] < buy_price:
            buy_price = prices[i]
        elif buy_price is not None and prices[i] - buy_price > max_profit:
            max_profit = prices[i] - buy_price
    
    return max_profit
        