class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            sorted_name="".join(sorted(s))

            if sorted_name not in res:
                res[sorted_name]=[]

            res[sorted_name].append(s)
        return list(res.values())