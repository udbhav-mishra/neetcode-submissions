from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hashmap = defaultdict(int)
        for char in s1: hashmap[char] += 1
        curr = defaultdict(int)

        i = 0
        j = len(s1)

        while j <= len(s2):
            for k in s2[i:j]:
                curr[k] += 1
            
            if curr == hashmap: return True
            curr.clear()
            i += 1
            j += 1
        
        return False