class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        num_rev_dict = defaultdict(list)
        max_frequency = 0
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        
        for num in nums_dict.keys():
            if nums_dict[num] > max_frequency:
                max_frequency = nums_dict[num]
            num_rev_dict[nums_dict[num]].append(num)

        # Using buckets to sort based on the frequency
        buckets = reversed(range(max_frequency + 1))
        results = []
        for element in buckets:
            if len(num_rev_dict[element]) > 0:
                results.extend(num_rev_dict[element])

        print(results)
        return results[:k]
        