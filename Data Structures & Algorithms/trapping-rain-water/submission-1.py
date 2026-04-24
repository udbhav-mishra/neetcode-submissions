class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n
        lmax = rmax = 0
        for i in range(n):
            lmax = max(height[i], lmax)
            prefix[i] = lmax
        
        for i in range(n - 1, -1, -1):
            rmax = max(height[i], rmax)
            suffix[i] = rmax

        water = 0
        for i in range(n):
            water += min(prefix[i], suffix[i]) - height[i]
        
        return water