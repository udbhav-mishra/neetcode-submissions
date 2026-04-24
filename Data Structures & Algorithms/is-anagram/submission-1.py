from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        maps = defaultdict(int)
        
        for i in range(len(s)):
            maps[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] in maps:
                maps[t[i]] -= 1
            
            else: return False

            if maps[t[i]] == 0: del maps[t[i]]
        
        return True if len(maps) == 0 else False