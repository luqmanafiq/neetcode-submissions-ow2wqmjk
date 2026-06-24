class Solution:
    def reorganizeString(self, s: str) -> str:
        char = Counter(s) # dict_items([('a', 1), ('x', 1), ('y', 2)])
        maxheap = [[-cnt, char] for char, cnt in char.items()] # ['y':-2,'x':-1,'a':-1]
        heapq.heapify(maxheap)
        result = []
        waitinglist = None

        while maxheap or waitinglist:
            if waitinglist and not maxheap:
                return ""

            cnt, char = heapq.heappop(maxheap)
            result.append(char)
            cnt += 1
            if waitinglist:
                heapq.heappush(maxheap, waitinglist)
                waitinglist = None
            if cnt != 0:
                waitinglist = [cnt, char]
        return "".join(result)