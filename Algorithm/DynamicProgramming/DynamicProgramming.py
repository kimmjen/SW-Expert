def solve_case(pairs):
    # 최대 y값의 합을 구합니다.
    max_y_sum = sum(y for x, y in pairs)

    # dp 배열을 초기화합니다.
    dp = [float('inf')] * (max_y_sum + 1)
    dp[0] = 0  # y의 합이 0일 때 x의 합은 0입니다.

    # 숫자 쌍을 순회하면서 dp 배열을 업데이트합니다.
    for x, y in pairs:
        for j in range(max_y_sum, y - 1, -1):
            dp[j] = min(dp[j], dp[j - y] + x)
    
    # Sx >= Sy를 만족하는 최소 Sx를 찾습니다.
    total_x = sum(x for x, y in pairs)
    for sy in range(max_y_sum + 1):
        if dp[sy] <= total_x - sy:
            return dp[sy]
    return -1

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
        idx += 1
        pairs = []
        for _ in range(N):
            x = int(data[idx])
            y = int(data[idx + 1])
            pairs.append((x, y))
            idx += 2
        result = solve_case(pairs)
        results.append(f"#{t + 1} {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()