from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tmap = defaultdict(int)
        window = defaultdict(int)
        ans = (float("inf"), 0, 0)
        for i in t:
            tmap[i] += 1

        need = len(tmap)
        formed = 0
        left = 0

        for right in range(len(s)):
            window[s[right]] += 1
            
            if s[right] in tmap and window[s[right]] == tmap[s[right]]:
                formed += 1

                while left <= right and formed == need:
                    if right - left + 1 < ans[0]:
                        ans = (right - left + 1, left, right)
                    
                    window[s[left]] -= 1
                    if s[left] in tmap and window[s[left]] < tmap[s[left]]:
                        formed -= 1
                    
                    left += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2]+1]