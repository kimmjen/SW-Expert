from collections import deque, defaultdict

def kahn_topological_sort(n, graph):
    in_degree = [0] * (n + 1)  # 각 노드의 진입 차수
    for u in range(1, n + 1):
        for v in graph[u]:
            in_degree[v] += 1
    
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    return topo_order

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for t in range(T):
        N = int(data[idx])
        M = int(data[idx + 1])
        idx += 2
        D = int(data[idx])
        idx += 1
        
        graph = defaultdict(list)
        for _ in range(M):
            u = int(data[idx])
            v = int(data[idx + 1])
            idx += 2
            graph[u].append(v)
        
        topo_order = kahn_topological_sort(N, graph)
        
        # 목적지까지의 경로만 추출
        try:
            d_index = topo_order.index(D)
            result_path = topo_order[:d_index + 1]
            results.append(f"#{t + 1} {' '.join(map(str, result_path[::-1]))}")
        except ValueError:
            results.append(f"#{t + 1} -1")  # 목적지가 존재하지 않는 경우
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()