class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_seen = float('inf')
        for p in prices:
            if p < min_seen:
                min_seen = p
            elif p > min_seen:
                curr_profit = p - min_seen
                max_profit = max(max_profit, curr_profit)
        return max_profit
