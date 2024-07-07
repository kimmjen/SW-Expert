def compare_numbers(test_cases):
    results = []
    for i, case in enumerate(test_cases):
        a, b = case
        if a > b:
            result = ">"
        elif a < b:
            result = "<"
        else:
            result = "="
        results.append(f"#{i+1} {result}")
    return results

def main():
    # 파일 입력 처리
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    T = int(lines[0].strip())
    test_cases = [list(map(int, line.strip().split())) for line in lines[1:T+1]]

    # 결과 출력
    results = compare_numbers(test_cases)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()