from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hashmap = defaultdict(int)
        ans = 0
        left = 0

        for right in range(len(s)):
            hashmap[s[right]] += 1
            diff = sum(hashmap.values()) - max(hashmap.values())
            
            while diff > k :
                hashmap[s[left]] -= 1
                diff = sum(hashmap.values()) - max(hashmap.values())
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans