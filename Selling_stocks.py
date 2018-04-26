def get_max_profit(stock_prices):
    # Calculate the max profit
    if len(stock_prices) < 2:
        print ("Invalid")

    min_price = stock_prices[0]
    cur_price = stock_prices[1]
    max_profit = cur_price - min_price

    for i in range(1, len(stock_prices)):
        cur_price = stock_prices[i]
        pot_profit = cur_price - min_price
        max_profit = max(pot_profit, max_profit)
        min_price = min(min_price, cur_price)
    return max_profit


