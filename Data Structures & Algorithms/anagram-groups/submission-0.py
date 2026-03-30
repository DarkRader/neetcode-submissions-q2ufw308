class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dic = {}
        for string in strs:
            sorted_chars = sorted(string)
            sorted_str = ''.join(sorted_chars)
            if sorted_str not in res_dic:
                res_dic[sorted_str] = [string]
            else:
                res_dic[sorted_str].append(string)

        res_list = []
        for str_list in res_dic:
            res_list.append(res_dic[str_list])

        return res_list
        