class Solution(object):
    def searchRange(self, nums, target):
        def findFirst():
            n = len(nums)
            low = 0
            high = n-1
            ans = -1
            while(low<=high):
                mid = (low + high)//2
                if nums[mid] == target:
                    ans = mid
                    high = mid-1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        def findLast():
            n = len(nums)
            low = 0
            high = n-1
            ans = -1
            while(low<=high):
                mid = (low + high)//2
                if nums[mid] == target:
                    ans = mid
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        return [findFirst(),findLast()]
