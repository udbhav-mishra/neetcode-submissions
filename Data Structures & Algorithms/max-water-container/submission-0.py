class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(len(heights)):
            for j in range(len(heights)):

                dist = abs(i - j)
                wall = min(heights[i], heights[j])
                water = dist * wall
                ans = max(ans, water)

        return ans