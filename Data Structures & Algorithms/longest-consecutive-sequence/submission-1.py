class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         
        if not nums: return 0
        s = set(nums)
        ans = 1

        for i in nums:
            count = 1
            while i + 1 in s:
                count += 1
                i += 1

            ans = max(count, ans)
        return ans 