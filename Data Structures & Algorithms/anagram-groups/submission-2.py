class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dic = defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            res_dic[sorted_str].append(string)

        res_list = []
        for str_list in res_dic:
            res_list.append(res_dic[str_list])

        return res_list
        