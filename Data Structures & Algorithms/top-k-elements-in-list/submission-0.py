from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = defaultdict(int)
        ans = []
        for i in range(len(nums)):
            map[nums[i]] += 1
        
        while k > 0:
            m = max(map, key = map.get)
            ans.append(m)
            del map[m]
            k -= 1

        return ans