class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        l1 = len(nums1)
        l2 = len(nums2)
        if l1 > l2:     #nums1 will always be smaller
            return self.findMedianSortedArrays(nums2, nums1)
        
        n = l1 + l2
        half = n // 2
        left, right = 0, len(nums1) - 1
        
        while True:
            i = (left + right) // 2 #mid of nums1
            j = half - i - 2        #mid of nums2

            Aleft = nums1[i] if i >= 0 else float("-inf")
            Aright = nums1[i + 1] if i + 1 < l1 else float("inf")
            Bleft = nums2[j] if j >= 0 else float("-inf")
            Bright = nums2[j + 1] if j + 1 < l2 else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if n % 2 == 0:  #for even length
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                return (min(Aright, Bright))
            
            elif Aleft > Bright: right = i - 1
            else: left = i + 1