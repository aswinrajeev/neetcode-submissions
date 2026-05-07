class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = []
        visited_indixes = set()
        for (i, str1) in enumerate(strs):
            if i in visited_indixes:
                continue

            curr_group = []
            curr_group.append(str1)
            visited_indixes.add(i)
            anagram_groups.append(curr_group)
            for j, str2 in enumerate(strs):
                if j in visited_indixes:
                    continue
                
                if self.areAnagrams(str1, str2):
                    visited_indixes.add(j)
                    curr_group.append(str2)
            
        return anagram_groups

                

    def areAnagrams(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False

        str1_map = {}
        str2_map = {}
        for i in range(len(str1)):
            str1_map[str1[i]] = str1_map.get(str1[i], 0) + 1
            str2_map[str2[i]] = str2_map.get(str2[i], 0) + 1

        return str1_map == str2_map
        