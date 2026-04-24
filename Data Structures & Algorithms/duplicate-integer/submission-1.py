from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        map = defaultdict(int)

        for i in range(len(nums)):
            map[nums[i]] += 1
        
        for i in map:
            if map[i] > 1:
                return True
        
        return False