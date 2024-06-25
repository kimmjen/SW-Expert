import heapq

def prim_mst(V, graph):
    visited = [False] * V
    min_heap = [(0, 0)]  # (weight, start_vertex)
    total_weight = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight

        for v in range(V):
            if graph[u][v] != 0 and not visited[v]:
                heapq.heappush(min_heap, (graph[u][v], v))

    return total_weight

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    V = int(data[idx + 1])
    idx += 2
    
    results = []
    
    for t in range(T):
        graph = []
        for i in range(V):
            row = list(map(int, data[idx:idx + V]))
            graph.append(row)
            idx += V
        
        mst_weight = prim_mst(V, graph)
        results.append(f"#{t + 1} {mst_weight}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()