class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []
        prod = 1
        for i in range(len(nums)):
            
            if i == 0: ans.append(1)
            else:
                prod *= nums[i - 1]
                ans.append(prod)

        prod = 1

        for i in range(len(nums) - 1, -1 , -1):

            if i != len(nums) - 1:
                prod *= nums[i + 1]
                ans[i] *= prod
        
        return ans