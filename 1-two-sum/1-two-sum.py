class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i in range(len(nums)):
            req = target - nums[i]
            if req in memo.keys():
                return [memo[req], i]
            memo[nums[i]] = i
            
        