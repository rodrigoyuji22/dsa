class Solution:
    # solução em O(n) -> Teoricamente O(3n)
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l_arr = [1] * n
        for i in range(1, n):
            l_arr[i] = nums[i-1] * l_arr[i-1]
        r_arr = [1] * n
        for j in range(n-2, -1, -1):
            r_arr[j] = nums[j+1] * r_arr[j+1]
        return [l_arr[k] * r_arr[k] for k in range(n)]

    # Solução em bruteforce
    def productExceptSelf2(self, nums):
        output = []
        n = len(nums)
        for i in range(n):
            product = 1
            for j in range(1, n):
                index = (i +j) % n
                product *= nums[index]
            output.append(product)
        return output
                
                