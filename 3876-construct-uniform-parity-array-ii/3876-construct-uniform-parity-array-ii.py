class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        
        odd=0
        even=0
        for x in nums1:
            if x&1:
                odd+=1
            else:
                even+=1
        
        if odd==0 or even==0:
            return True
        return nums1[0]&1==1