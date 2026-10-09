class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            temp = prices[:]

            for start, end, price in flights:
                if prices[start] != float('inf'):
                    temp[end] = min(
                        temp[end],
                        prices[start] + price
                    )

            prices = temp

        if prices[dst] == float('inf'):
            return -1

        return prices[dst]
        
        
        