class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for num in nums]
        suffix = [1 for num in nums]
        results = [0 for num in nums]
        n = len(nums)
        for i in range(n):
            p = i - 1 if i > 0 else 0
            s = n - i if i > 0 else n - 1
            prefix[i] = prefix[p] * nums[i]
            suffix[n - 1 - i] = suffix[s] * nums[n - 1 - i]

        print(prefix, suffix)
        for i in range(n):
            p = prefix[i - 1] if i > 0 else 1
            s = suffix[i + 1] if i < n - 1 else 1
            results[i] = p * s

        return results