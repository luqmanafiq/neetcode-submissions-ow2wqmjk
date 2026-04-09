class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for alphabet in strs:
            sorted_strs = ''.join(sorted(alphabet))
            store[sorted_strs].append(alphabet)
        return list(store.values())