from queue import PriorityQueue

def dijk(g,n,s):

  vis = [False] * n
  dist = [float('inf')] * n
  dist[s] = 0
  pq = PriorityQueue()
  pq.put((0,s))

  while not pq.empty():
    minVal,index= pq.get()

    vis[index] = True
    for edge in g[index]:
      neighbor = edge[0]
      weight = edge[1]
      if vis[neighbor]:
        continue
      newDist = dist[index] + weight
      if newDist < dist[neighbor]:
        dist[neighbor] = newDist
        pq.put((newDist, neighbor))

  return dist
graph = {
    0: [[1,4], [2,1]],
    1: [[3,1]],
    2: [[1,2],[3,5]],
    3: [[4,3]],
    4 : []
}
n = len(graph)
s = 0
dijk(graph,n,s)