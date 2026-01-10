class Solution:
    # O(n) 70% 47ms
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) >= 1:
            _max = 1
        else:
            return 0
            
        _set = set(nums)
        for num in _set:
            if num -1 in _set:
                continue
            else:
                next_ = num + 1
                count = 1
                while next_ in _set:
                    next_ += 1
                    count += 1
                    _max = max(_max, count)
        return _max
                    
    # O(nlogn) 98.91% 35ms
    def longestConsecutive2(self, nums: list[int]) -> int:
        if len(nums) >= 1:
            count, _max = 1, 1
        else:
            return 0
        
        nums = sorted(set(nums))
        for i in range(len(nums)):
            if nums[i] == nums[i-1]+1:
                count += 1
                _max = max(_max, count)
            else:
                count = 1
        return max(_max, count)