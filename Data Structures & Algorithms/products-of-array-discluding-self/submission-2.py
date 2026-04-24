class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prod = 1

        if 0 not in nums:
            prod = 1
            for i in nums:
                prod *= i
            
            for i in nums:
                ans.append(prod // i)

        else:
            if nums.count(0) > 1:
                ans = [0] * len(nums)
            
            else:

                for i in nums:
                    if i != 0:
                        prod *= i
                
                for i in nums:
                    if i == 0: ans.append(prod)
                    else: ans.append(0)

        return ans