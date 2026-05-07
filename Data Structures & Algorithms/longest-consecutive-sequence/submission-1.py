class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_count = 0
        for num in nums:
            length = 1
            if num - 1 not in num_set:
                while (num + length) in num_set:
                    length += 1

                max_count = max(max_count, length)

        return max_count