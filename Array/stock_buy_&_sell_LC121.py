class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = float('inf')
        max_pro = 0
        for i in range(n):
            min_price = min(min_price, prices[i])
            max_pro = max(max_pro, prices[i]-min_price)
        return max_pro
