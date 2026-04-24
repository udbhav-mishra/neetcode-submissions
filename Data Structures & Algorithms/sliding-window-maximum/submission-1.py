from collections import defaultdict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window = defaultdict(int)

        i = 0
        j = k
        ans = []

        while j <= len(nums):
            ans.append(max(nums[i:j]))

            i += 1
            j += 1
        
        return ans