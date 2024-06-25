def floyd_warshall(n, edges):
    # 거리 행렬 초기화
    dist = [[float('inf')] * n for _ in range(n)]
    
    # 자기 자신으로 가는 거리는 0으로 설정
    for i in range(n):
        dist[i][i] = 0
    
    # 주어진 간선 정보로 거리 행렬 초기화
    for u, v, w in edges:
        dist[u-1][v-1] = w
    
    # 플로이드-워셜 알고리즘 적용
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for t in range(T):
        num_vertices = int(data[idx])
        idx += 1
        num_edges = int(data[idx])
        idx += 1
        
        edges = []
        
        for _ in range(num_edges):
            u = int(data[idx])
            v = int(data[idx + 1])
            cost = int(data[idx + 2])
            idx += 3
            edges.append((u, v, cost))
        
        dist = floyd_warshall(num_vertices, edges)
        result = f"#{t + 1}\n"
        
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][j] == float('inf'):
                    result += "INF "
                else:
                    result += f"{dist[i][j]} "
            result = result.strip() + "\n"
        
        results.append(result.strip())
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()