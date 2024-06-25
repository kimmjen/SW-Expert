from collections import deque

def bfs_shortest_path(map, start_row, start_col, end_row, end_col, R, C):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향
    
    queue = deque([(start_row, start_col, 1)])  # 시작점과 거리(1)를 큐에 넣음
    visited = [[False] * C for _ in range(R)]
    visited[start_row][start_col] = True
    
    while queue:
        r, c, dist = queue.popleft()
        
        if r == end_row and c == end_col:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < R and 0 <= nc < C:  # 범위 내에 있고
                if map[nr][nc] == 1 and not visited[nr][nc]:  # 길이고 방문하지 않았으면
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))
    
    return -1  # 도달할 수 없는 경우

def main():
    import sys
    input = sys.stdin.read().splitlines()
    
    index = 0
    test_cases = int(input[index])
    index += 1
    results = []
    
    for t in range(test_cases):
        R, C = map(int, input[index].split())
        index += 1
        
        # 지도 입력 받기
        map = []
        for i in range(R):
            map.append(list(map(int, input[index].split())))
            index += 1
        
        # 시작점과 도착점 설정 (입력에서는 1-indexed이므로 0-indexed로 변환)
        start_row, start_col = 0, 0
        end_row, end_col = R - 1, C - 1
        
        # BFS로 최단 경로 길이 찾기
        shortest_distance = bfs_shortest_path(map, start_row, start_col, end_row, end_col, R, C)
        
        results.append(f"#{t + 1} {shortest_distance}")
    
    # 결과 출력
    for result in results:
        print(result)

if __name__ == "__main__":
    main()