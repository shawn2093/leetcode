class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        smallest = prices[0]
        for i in prices:
            smallest = min(smallest, i)
            profit.append(i - smallest)
        return (max(profit))