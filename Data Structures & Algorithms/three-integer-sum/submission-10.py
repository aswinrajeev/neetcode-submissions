class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []

        for i, num in enumerate(nums):

            if i > 0 and num == nums[i-1]:
                continue

            start = i + 1
            end = len(nums) - 1
            while start < end:

                sum = num + nums[start] + nums[end]
                if sum  == 0:
                    solutions.append([num, nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while nums[start] == nums[start-1] and start < end:
                        start += 1
                        continue

                elif sum > 0:
                    end -= 1
                else:
                    start += 1
        
        return solutions
