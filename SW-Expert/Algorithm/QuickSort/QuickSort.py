def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# 입력 데이터를 처리하고 퀵 정렬을 수행하는 메인 함수
def main():
    # 예제 입력 데이터
    test_cases = int(input("Enter the number of test cases: "))  # 전체 테스트 케이스 수
    for _ in range(test_cases):
        data_size = int(input("Enter the size of the data: "))  # 데이터 크기
        data = list(map(int, input("Enter the data: ").split()))  # 데이터 리스트
        sorted_data = quick_sort(data)  # 퀵 정렬 수행
        print("Sorted data:", " ".join(map(str, sorted_data)))  # 정렬된 데이터 출력

if __name__ == "__main__":
    main()