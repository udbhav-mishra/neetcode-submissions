class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        hashmap = set()
        left = 0

        for right in range(len(s)):
            while s[right] in hashmap:
                hashmap.remove(s[left])
                left += 1
            ans = max(ans, right -left + 1)

            if s[right] not in hashmap:
                hashmap.add(s[right])
        
        return ans