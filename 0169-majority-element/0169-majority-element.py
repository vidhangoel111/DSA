class Solution:
    def majorityElement(self, nums):
        n = len(nums)

        mp = {}

        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1

        for num, count in mp.items():
            if count > n // 2:
                return num