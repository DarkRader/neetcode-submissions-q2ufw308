class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index = 0
        max_profit = 0

        for i, p in enumerate(prices):
            if i + 1 != len(prices):
                if prices[i + 1] > p:
                    index = i
                    break
            if i == len(prices) - 1:
                return max_profit

        for i, p in enumerate(prices[index:], start=index):
            print(f"{i}, -> {p}")
            z = i + 1
            while z != len(prices):
                max_profit = max(max_profit, prices[z] - p)
                z += 1
        
        return max_profit