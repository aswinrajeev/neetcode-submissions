class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for str in strs:
            str_sorted = "".join(sorted(str))
            groups[str_sorted].append(str)
        return list(groups.values())
        