class Solution(object):
    def check(self, nums):
        decreases = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                decreases+=1
                if decreases > 1:
                    return False
        return True