class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            time = 0

            for i in piles:
                time += i // mid
                if i % mid != 0: time += 1
            
            if time <= h: right = mid
            else: left = mid + 1
        
        return left