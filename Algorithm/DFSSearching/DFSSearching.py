def dfs(graph, current, end, visited, path_length):
    if current == end:
        return path_length
    
    visited[current] = True
    min_distance = float('inf')
    
    for neighbor in graph[current]:
        if not visited[neighbor]:
            distance = dfs(graph, neighbor, end, visited, path_length + 1)
            if distance < min_distance:
                min_distance = distance
    
    visited[current] = False  # 백트래킹
    
    return min_distance

def main():
    import sys
    input = sys.stdin.read().splitlines()
    
    index = 0
    test_cases = int(input[index])
    index += 1
    results = []
    
    for t in range(test_cases):
        num_vertices, num_edges, start, end = map(int, input[index].split())
        index += 1
        
        graph = [[] for _ in range(num_vertices + 1)]
        
        for _ in range(num_edges):
            u, v = map(int, input[index].split())
            graph[u].append(v)
            graph[v].append(u)
            index += 1
        
        visited = [False] * (num_vertices + 1)
        shortest_distance = dfs(graph, start, end, visited, 0)
        
        if shortest_distance == float('inf'):
            results.append(f"#{t + 1} -1")
        else:
            results.append(f"#{t + 1} {shortest_distance}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()