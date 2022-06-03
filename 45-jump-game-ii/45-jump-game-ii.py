class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [None] * (len(nums))
        dp[len(nums)-1] = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > 0:
                minn = 999999
                for j in range(1, nums[i]+1):
                    if i+j >= len(nums):
                        break
                    if dp[i+j] != None:
                        minn = min(minn, dp[i+j])
                if minn != 999999:
                    dp[i] = minn + 1
        return dp[0]