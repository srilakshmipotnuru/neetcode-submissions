import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[-num for num in nums]
        self.k=k
        heapq.heapify(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,-val)
        arr=[]
        for i in range(self.k):
            arr.append(heapq.heappop(self.heap))
        ans=-arr[-1]
        while arr:
            heapq.heappush(self.heap,arr.pop())
        return ans
                

