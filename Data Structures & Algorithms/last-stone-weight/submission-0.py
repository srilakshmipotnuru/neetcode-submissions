import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-num for num in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            x,y=-heapq.heappop(heap),-heapq.heappop(heap)
            if x!=y:
                heapq.heappush(heap,y-x)
        return -heap[0] if len(heap)==1 else 0
        