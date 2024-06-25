from collections import defaultdict

def process_graph_queries(test_cases):
    results = []
    for case_index, (V, E, Q, edges, queries) in enumerate(test_cases):
        graph = defaultdict(list)
        
        # 간선 정보로 그래프 구성
        for i in range(0, len(edges), 2):
            u = edges[i]
            v = edges[i + 1]
            graph[u].append(v)
            graph[v].append(u)
        
        # 정점의 인접 정점을 사전 순으로 정렬
        for key in graph:
            graph[key].sort()
        
        # 쿼리 처리
        result = [f"#{case_index + 1}"]
        for query in queries:
            if query in graph:
                result.append(" ".join(map(str, graph[query])))
            else:
                result.append("")
        
        results.append("\n".join(result))
    
    return results

if __name__ == "__main__":
    input_file = 'input.txt'
    
    # 파일에서 입력 읽기
    with open(input_file, 'r') as file:
        data = file.read().strip().split('\n')
        
    test_case_count = int(data[0].strip())
    index = 1
    test_cases = []
    
    for _ in range(test_case_count):
        V, E, Q = map(int, data[index].strip().split())
        edges = []
        for i in range(1, E + 1):
            u, v = map(int, data[index + i].strip().split())
            edges.extend([u, v])
        
        queries = []
        for i in range(E + 1, E + Q + 1):
            queries.append(int(data[index + i].strip()))
        
        test_cases.append((V, E, Q, edges, queries))
        index += E + Q + 1
    
    outputs = process_graph_queries(test_cases)
    for output in outputs:
        print(output)