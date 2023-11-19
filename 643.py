class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currsum = sum(nums[0:k])
        maxsum = sum(nums[0:k])
        for i in range(k, len(nums)):
            currsum = currsum - nums[i-k] + nums[i]
            maxsum = max(maxsum, currsum)
        return maxsum/k

        