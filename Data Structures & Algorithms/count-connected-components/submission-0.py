class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        m=edges
        adj= [[] for i in range(n)]
        for edge in m:
            u,v = edge
            adj[u].append(v)
            adj[v].append(u)
            
        visited= [False]*n
        count=0
        for i in range(n):
            if not visited[i]:
              count+=1
              queue=deque()
              queue.append(i)
              visited[i]=True
              while queue:
                node = queue.popleft()
                for child in adj[node]:
                  if not visited[child]:
                    visited[child]=True
                    queue.append(child)
        return count
        