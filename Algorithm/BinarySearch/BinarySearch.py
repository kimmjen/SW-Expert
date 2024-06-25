def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    # 입력을 받기 위해 사용자가 입력하는 형식을 흉내냅니다.
    test_cases = int(input("Enter the number of test cases: "))
    results = []

    for t in range(test_cases):
        num_elements = int(input("Enter the number of elements in array: "))
        num_searches = int(input("Enter the number of numbers to search: "))
        
        sorted_array = list(map(int, input("Enter the sorted array: ").split()))
        search_numbers = list(map(int, input("Enter the numbers to search: ").split()))
        
        result = []
        for number in search_numbers:
            result.append(binary_search(sorted_array, number))
        
        results.append(f"#{t + 1} " + " ".join(map(str, result)))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()