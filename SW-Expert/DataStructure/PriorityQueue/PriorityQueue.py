from queue import PriorityQueue

def process_priority_queue_operations(test_cases):
    results = []
    for case_index, case in enumerate(test_cases):
        n, numbers = case
        priority_queue = PriorityQueue()
        
        # 숫자들을 우선순위 큐에 넣음
        for number in numbers:
            priority_queue.put(number)
        
        ordered_numbers = []
        # 우선순위 큐에서 숫자들을 꺼내어 리스트에 추가
        while not priority_queue.empty():
            ordered_numbers.append(priority_queue.get())
        
        # 결과 문자열 생성
        result = f"#{case_index + 1} " + " ".join(map(str, ordered_numbers))
        results.append(result)
    
    return results

if __name__ == "__main__":
    input_file = 'input.txt'
    
    # 파일에서 입력 읽기
    with open(input_file, 'r') as file:
        data = file.read().strip().split('\n')
    
    test_case_count = int(data[0])
    index = 1
    test_cases = []
    
    # 테스트 케이스 처리
    for _ in range(test_case_count):
        n = int(data[index])
        numbers = list(map(int, data[index + 1].split()))
        test_cases.append((n, numbers))
        index += 2
    
    # 우선순위 큐 연산 수행 및 결과 출력
    outputs = process_priority_queue_operations(test_cases)
    for output in outputs:
        print(output)