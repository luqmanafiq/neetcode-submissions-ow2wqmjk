class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}
        for word in strs:
            sorted_strs="".join(sorted(word))
            if sorted_strs in anagrams:
                anagrams[sorted_strs].append(word)
            else:
                anagrams[sorted_strs]=[word]
        return list(anagrams.values())