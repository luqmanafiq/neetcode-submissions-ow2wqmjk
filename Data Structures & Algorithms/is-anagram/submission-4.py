class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shash=defaultdict(int)
        thash=defaultdict(int)
        for i in s:
            shash[i]+=1
        for j in t:
            thash[j]+=1
        if shash == thash:
            return True
        return False
                
                