from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = defaultdict(list)

        for i in strs:
            key = tuple(sorted(i))
            map[key].append(i)

        return list(map.values())