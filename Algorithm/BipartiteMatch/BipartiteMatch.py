from collections import defaultdict

class BipartiteGraph:
    def __init__(self, n, m):
        self.n = n  # A 그룹의 크기
        self.m = m  # B 그룹의 크기
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bpm(self, u, match_r, seen):
        for v in self.graph[u]:
            if not seen[v]:
                seen[v] = True
                if match_r[v] == -1 or self.bpm(match_r[v], match_r, seen):
                    match_r[v] = u
                    return True
        return False

    def max_bpm(self):
        match_r = [-1] * (self.m + 1)
        result = 0
        for i in range(1, self.n + 1):
            seen = [False] * (self.m + 1)
            if self.bpm(i, match_r, seen):
                result += 1
        return result

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for t in range(T):
        n = int(data[idx])
        idx += 1
        m = int(data[idx])
        idx += 1
        e = int(data[idx])
        idx += 1
        
        graph = BipartiteGraph(n, m)
        
        for _ in range(e):
            u = int(data[idx])
            v = int(data[idx + 1])
            idx += 2
            graph.add_edge(u, v)
        
        max_matching = graph.max_bpm()
        results.append(f"#{t + 1} {max_matching}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()