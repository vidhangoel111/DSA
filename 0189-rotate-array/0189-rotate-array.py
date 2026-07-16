class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k%=n
        left = 0
        right = n-1
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1
            right-=1
        
        l = 0
        r = k-1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        
        lef = k
        rig = n-1
        while lef < rig:
            nums[lef],nums[rig] = nums[rig],nums[lef]
            lef+=1
            rig-=1

        
        
        