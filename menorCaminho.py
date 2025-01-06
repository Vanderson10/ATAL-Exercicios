import sys
import heapq

input = sys.stdin.readline
def takeInt(): return int(input())
def takeInts(): return map(int, input().split())
def takeList(): return list(map(int, input().split()))


mod = int(1e9) + 7

n, e = takeInts()
graph = [[] for j in range(n + 1)]
for _ in range(e):
    u, v, w = takeInts()
    graph[u].append((v, w))


def dijkstras(graph, start):
    dist = [float("inf") for i in range(n + 1)]
    vis = [False for i in range(n + 1)]
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, start))
    dist[start] = 0

    while heap:
        d, cur = heapq.heappop(heap)
        if vis[cur] == True:
            continue
        vis[cur] = True
        for i, w in graph[cur]:
            if d + w < dist[i]:
                dist[i] = d + w
                heapq.heappush(heap, (dist[i], i))
    return dist


print(*dijkstras(graph, 1)[1:])
