class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        num_rev_dict = defaultdict(list)
        result = []
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        
        for num in nums_dict.keys():
            num_rev_dict[nums_dict[num]].append(num)

        for element in sorted(num_rev_dict.keys(), reverse=True):
            result.extend(num_rev_dict[element])

        return result[:k]
        