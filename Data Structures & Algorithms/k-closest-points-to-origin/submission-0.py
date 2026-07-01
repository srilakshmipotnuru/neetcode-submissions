import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for point in points:
            x,y=point
            dist=math.sqrt(x*x+y*y)
            heapq.heappush(heap, (-dist,[x,y]))
            while len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for tup in heap:
            res.append(tup[1])
        return res



        