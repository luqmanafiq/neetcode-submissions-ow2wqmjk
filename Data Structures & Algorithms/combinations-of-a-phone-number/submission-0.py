class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToNumber = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        
        result = []
        store = []

        def backtrack(i):
            if i == len(digits):
                result.append("".join(store))
                return
            for char in digitToNumber[digits[i]]:
                store.append(char)
                backtrack(i+1)
                store.pop()
        backtrack(0)
        return result