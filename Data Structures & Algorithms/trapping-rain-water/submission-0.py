class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0        
        max_l = 0
        prefix = []
        for i in range(len(height)):
            max_l = max(max_l, height[i])
            prefix.append(max_l)
        
        max_r = 0
        suffix = []
        for i in range(len(height) - 1, -1, -1):
            max_r = max(max_r, height[i])
            suffix.insert(0, max_r)
        
        
        for i in range(len(height)):
            wall = min(prefix[i], suffix[i])
            if wall > height[i]:
                water += wall - height[i]
        
        return water