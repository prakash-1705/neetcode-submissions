class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        element = {}
        for i in range(len(nums)):
            if (target-nums[i]) in element:
                return [element[target-nums[i]], i]
            else:
                element[nums[i]] = i