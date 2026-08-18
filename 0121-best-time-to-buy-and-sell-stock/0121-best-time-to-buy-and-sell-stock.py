class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        max_profit = 0
        min_buy_price = prices[0]
        for i in range(n):
            if prices[i] < min_buy_price:
                min_buy_price = prices[i]
            potential_profit = prices[i] - min_buy_price

            if potential_profit > max_profit:
                max_profit = potential_profit
        return max_profit
        
        