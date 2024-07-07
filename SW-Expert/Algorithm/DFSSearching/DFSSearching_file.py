def dfs_shortest_path(graph, start, end, visited):
    if start == end:
        return 0
    
    visited[start] = True
    min_distance = float('inf')
    
    for neighbor in graph[start]:
        if not visited[neighbor]:
            distance = dfs_shortest_path(graph, neighbor, end, visited)
            if distance != -1:  # 도착점에 도달한 경우
                min_distance = min(min_distance, distance + 1)
    
    visited[start] = False  # 백트래킹
    
    if min_distance == float('inf'):
        return -1
    else:
        return min_distance

def main():
    results = []
    
    with open('input.txt', 'r') as file:
        input_data = file.read().splitlines()
        print(input_data)
    
    index = 0
    test_cases = int(input_data[index])
    index += 1
    
    for t in range(test_cases):
        num_vertices, num_edges, start, end = map(int, input_data[index].split())
        index += 1
        
        graph = [[] for _ in range(num_vertices + 1)]
        
        for _ in range(num_edges):
            u, v = map(int, input_data[index].split())
            graph[u].append(v)
            graph[v].append(u)
            index += 1
        
        visited = [False] * (num_vertices + 1)
        shortest_distance = dfs_shortest_path(graph, start, end, visited)
        
        results.append(f"#{t + 1} {shortest_distance}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()