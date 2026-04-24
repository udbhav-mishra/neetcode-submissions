class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)

        a.sort()
        b.sort()

        return True if a == b else False