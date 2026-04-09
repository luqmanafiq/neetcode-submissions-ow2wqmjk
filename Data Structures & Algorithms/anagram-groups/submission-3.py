class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for word in strs:
            count = [0]*26
            for alphabet in word:
                index = ord(alphabet) - ord('a')
                count[index] += 1
            key = tuple(count)
            store[key].append(word)
        return list(store.values())