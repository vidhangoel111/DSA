class Solution(object):
    def singleNonDuplicate(self, nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            # Make mid even
            if mid % 2 == 1:
                mid -= 1

            # Pair is intact → single is on the right
            if nums[mid] == nums[mid + 1]:
                low = mid + 2

            # Pair is broken → single is on the left or at mid
            else:
                high = mid

        return nums[low]
        