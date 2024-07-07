import heapq
import sys

def dijkstra(graph, start, end):
    # 각 노드까지의 최단 거리를 저장하는 딕셔너리. 처음에는 모든 노드까지의 거리를 무한대(float('inf'))로 설정합니다.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    #  우선순위 큐(최소 힙)를 사용하여 현재 노드까지의 거리를 추적합니다. 시작 정점의 거리를 0으로 설정하고 큐에 추가합니다.
    priority_queue = [(0, start)]
    
    while priority_queue: # 큐가 빌 때까지 반복합니다.
        # 큐에서 현재 노드와 거리를 꺼냅니다.
        current_distance, current_node = heapq.heappop(priority_queue)
        # 현재 노드까지의 최단 경로가 이미 기록된 거리보다 크다면 무시합니다.
        if current_distance > distances[current_node]:
            continue
        # 현재 노드의 모든 인접 노드를 확인합니다.
        for neighbor, weight in graph[current_node].items():
            # 현재 노드를 거쳐 인접 노드까지 가는 거리를 계산합니다.
            distance = current_distance + weight
            # 계산된 거리가 기존 거리보다 짧다면 갱신합니다.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # 갱신된 노드를 큐에 추가합니다.
                heapq.heappush(priority_queue, (distance, neighbor))
    # 도착 정점까지의 최단 거리를 반환합니다.
    return distances[end]

def main():
    input = sys.stdin.read # 입력 데이터를 한 번에 읽어 들입니다.
    data = input().split() # 입력 데이터를 공백으로 나누어 리스트로 저장합니다.
    
    idx = 0 # 입력 데이터를 순차적으로 읽어오기 위한 인덱스입니다.
    T = int(data[idx]) # 테스트 케이스의 개수를 읽어옵니다.
    idx += 1
    
    results = []
    
    for t in range(T): # 각 테스트 케이스에 대해 반복합니다.
        num_vertices = int(data[idx]) # 정점의 개수를 읽어옵니다.
        start_vertex = int(data[idx + 1]) # 시작 정점을 읽어옵니다.
        end_vertex = int(data[idx + 2]) # 도착 정점을 읽어옵니다.
        idx += 3
        
        num_edges = int(data[idx]) # 간선의 개수를 읽어옵니다.
        idx += 1
        
        graph = {i: {} for i in range(1, num_vertices + 1)} # 그래프를 인접 리스트로 초기화합니다.
        
        for _ in range(num_edges): # 각 간선을 읽어 그래프에 추가합니다.
            u = int(data[idx])
            v = int(data[idx + 1])
            cost = int(data[idx + 2])
            idx += 3
            graph[u][v] = cost # 간선의 시작 정점, 도착 정점, 가중치를 그래프에 추가합니다.
        
        result = dijkstra(graph, start_vertex, end_vertex) # 다익스트라 알고리즘을 사용하여 최단 경로를 계산합니다.
        results.append(f"#{t + 1} {result}") # 결과를 리스트에 저장합니다.
    
    for result in results: # 모든 결과를 출력합니다.
        print(result)

if __name__ == "__main__":
    main()