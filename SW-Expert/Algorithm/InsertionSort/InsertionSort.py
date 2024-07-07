def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 입력 데이터를 처리하고 삽입 정렬을 수행하는 메인 함수
def main():
    # 예제 입력 데이터
    test_cases = int(input("Enter the number of test cases: "))  # 전체 테스트 케이스 수
    for _ in range(test_cases):
        data_size = int(input("Enter the size of the data: "))  # 데이터 크기
        data = list(map(int, input("Enter the data: ").split()))  # 데이터 리스트
        sorted_data = insertion_sort(data)  # 삽입 정렬 수행
        print("Sorted data:", " ".join(map(str, sorted_data)))  # 정렬된 데이터 출력

if __name__ == "__main__":
    main()