class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in hash:
                hash[sorted_str].append(s)
            else:
                hash[sorted_str] = [s]
        return list(hash.values())