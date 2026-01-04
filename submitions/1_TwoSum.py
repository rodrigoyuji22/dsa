class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        _map = {}
        for i in range (len(nums)):
            resultant = target - nums[i]
            if resultant in _map:
                return [_map[resultant], i]
            _map[nums[i]] = i
        return []