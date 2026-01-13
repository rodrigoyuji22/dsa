class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        if len(numbers) <= 1:
            return []

        l, r = 0, len(numbers)-1
        while l < r:
            soma = numbers[l] + numbers[r]
            if soma == target:
                return [l+1, r+1]

            elif soma > target:
                r -= 1

            else:
                l += 1

        return []