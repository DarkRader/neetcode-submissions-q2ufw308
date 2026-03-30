class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dic = defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            res_dic[sorted_str].append(string)

        return list(res_dic.values())
        