class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        # Creating an array to store the values and its index
        arr = [] 
        for i in range(n):
            arr.append((nums[i],i))
        # Now sort the arr[] based on the values.
        arr.sort()
        r = len(arr)
        
        left = 0
        right = r-1
        while(left<=right):
            sum = arr[left][0] + arr[right][0]
            if(sum == target):
                return arr[left][1],arr[right][1]
            elif(sum < target):
                left+=1
            else:
                right-=1
            

        