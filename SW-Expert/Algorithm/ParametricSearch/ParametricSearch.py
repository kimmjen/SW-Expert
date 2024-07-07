def can_make_n_ribbons(ribbons, length, N):
    count = 0
    for ribbon in ribbons:
        count += ribbon // length
        if count >= N:
            return True
    return False

def find_max_length(ribbons, N):
    left, right = 1, max(ribbons)  # 길이의 범위 설정: 1부터 가장 긴 리본 길이까지
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_make_n_ribbons(ribbons, mid, N):
            result = mid  # 현재 길이로 N개 이상의 리본을 만들 수 있음
            left = mid + 1  # 더 큰 길이 탐색
        else:
            right = mid - 1  # 현재 길이로는 N개 이상의 리본을 만들 수 없음
    
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []

    for case in range(T):
        K = int(data[index])
        N = int(data[index + 1])
        ribbons = []
        for i in range(K):
            ribbons.append(int(data[index + 2 + i]))
        
        max_length = find_max_length(ribbons, N)
        results.append(f"#{case + 1} {max_length}")
        
        index += 2 + K

    for result in results:
        print(result)

if __name__ == "__main__":
    main()