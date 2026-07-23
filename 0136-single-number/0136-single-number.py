class Solution(object):
    def singleNumber(self,nums):
        n = len(nums)
        XOR = 0
        for i in range(n):
            XOR = XOR ^ nums[i]
        return XOR

                
                            
        