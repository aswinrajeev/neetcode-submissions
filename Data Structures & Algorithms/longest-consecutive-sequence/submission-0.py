class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        min = 1000
        max = -1
        for num in nums:
            if num > max:
                max = num
            
            if num < min:
                min = num

        length = max + 1 - min
        arr = [0] * length

        for num in nums:
            arr[num-min] = 1

        max_count = 0
        curr_count = 0
        for i in range(0, length):
            if arr[i] == 1:
                curr_count += 1
                if curr_count > max_count:
                    max_count = curr_count
            else:
                curr_count = 0
        
        return max_count