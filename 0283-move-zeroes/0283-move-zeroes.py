class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        read = 0
        write = 0
        for i in range(n):
            if(nums[read]!=0):
                nums[read],nums[write]=nums[write],nums[read]
                write+=1
                read+=1
            else:
                read+=1
                
                  