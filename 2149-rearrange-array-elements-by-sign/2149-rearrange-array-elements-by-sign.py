class Solution(object):
    def rearrangeArray(self, nums):
        positive = []
        negative = []

        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)

        ans = []

        for i in range(len(positive)):
            ans.append(positive[i])
            ans.append(negative[i])

        return ans

