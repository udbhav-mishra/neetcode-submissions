class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []      #(index, height)

        for i in range(len(heights)):
            start = i

            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, heights[i]))
        
        for i in stack:
            maxArea = max(maxArea, i[1] * (len(heights) - i[0]))
        
        return maxArea
