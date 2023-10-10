def maxProfit(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0] # initialize minimum price to be first position in array
    max_profit = 0 # initialize profit as 0 for selling on same day

    for price in prices: # loop through each price
        if price < min_price: # if the price of that day is less min
            min_price = price # assign new variable to min_price
        profit = price - min_price # assign profit to new day value minus minimum
        if max_profit < profit: # if max profit is now less
            max_profit = profit # reassign max-profit

    return max_profit




if __name__ == '__main__':
    prices = [7,6,4,3,1]
    print(maxProfit(prices))


