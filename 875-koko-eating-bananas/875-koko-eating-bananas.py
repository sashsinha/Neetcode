class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo < hi:
            mi = (lo + hi) // 2
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile / mi)
            if hours_spent <= h:
                hi = mi
            else:
                lo = mi + 1
        return lo
