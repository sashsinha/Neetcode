class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        min_speed = right
        while left <= right:
            mid = left + (right - left) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            if hours > h:
                left = mid + 1
            else:
                min_speed = min(min_speed, mid)
                right = mid - 1
        return min_speed
