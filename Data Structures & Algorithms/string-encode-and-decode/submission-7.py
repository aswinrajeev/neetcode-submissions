class Solution:

    def encode(self, strs: List[str]) -> str:
        prefix = ""
        data = ""
        for s in strs:
            prefix += str(len(s)) + "_"
            data += s
        return prefix[:-1] + "&&" + data

    def decode(self, s: str) -> List[str]:
        print(s)
        data_arr = s.split("&&", 1)
        data = data_arr[1]
        prefix = data_arr[0]

        strs = []

        last_index = 0
        for seq in prefix.split("_"):
            if seq != '':
                end = last_index + int(seq)
                print(last_index, "-", end)
                strs.append(data[last_index:end])
                last_index = end

        return strs
