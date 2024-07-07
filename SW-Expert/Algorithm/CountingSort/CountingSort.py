def counting_sort(arr):
    if not arr:
        return []
    
    max_val = max(arr)  # 최대 값 찾기
    count = [0] * (max_val + 1)  # 빈도 저장을 위한 카운트 배열
    
    # 각 숫자의 빈도 계산
    for num in arr:
        count[num] += 1
    
    # 누적합 계산
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # 정렬된 배열 생성
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output

def main():
    test_cases = int(input("Enter the number of test cases: "))  # 전체 테스트 케이스 수
    for _ in range(test_cases):
        data_size = int(input("Enter the size of the data: "))  # 데이터 크기
        data = list(map(int, input("Enter the data: ").split()))  # 데이터 리스트
        sorted_data = counting_sort(data)  # 카운팅 정렬 수행
        print("Sorted data:", " ".join(map(str, sorted_data)))  # 정렬된 데이터 출력

if __name__ == "__main__":
    main()