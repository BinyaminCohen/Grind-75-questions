# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class BuySellStocks(object):
    def max_profit(self, prices):

        lowest_price = min(prices)
        biggest_price = max(prices)

        lowest_price_idx = prices.index(lowest_price)
        biggest_price_idx = prices.index(biggest_price)

        if lowest_price_idx < biggest_price_idx:
            print(f"The max profit is: {biggest_price - lowest_price} ")

        else:
            max_value = max(prices[lowest_price_idx:])
            print(f"The max profit is: {max_value - lowest_price} ")


BuySellStocks.max_profit(BuySellStocks, [1, 7, 5, 3, 6, 4])

BuySellStocks.max_profit(BuySellStocks, [7, 6, 4, 3, 1])
