class Solution(object):
    def searchInsert(self, nums, target):
       n = len(nums)
       low = 0
       high = n-1
       while(low <= high):
        mid = (low + high)//2
        if(target == nums[mid]):
            return mid
        elif(target > nums[mid]):
            low = mid + 1
        else:
            high = mid - 1
       return low