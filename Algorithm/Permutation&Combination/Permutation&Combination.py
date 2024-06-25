import itertools

def solve_case(s, n, k):
    # 순열 출력
    permutations = list(itertools.permutations(s, n))
    print(f"#{1}")
    for perm in permutations:
        print(''.join(perm))
    
    # 조합 출력
    combinations = list(itertools.combinations(s, k))
    for comb in combinations:
        print(''.join(comb))

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for t in range(T):
        s = data[idx]
        idx += 1
        n = int(data[idx])
        idx += 1
        k = int(data[idx])
        idx += 1
        solve_case(s, n, k)

if __name__ == "__main__":
    main()