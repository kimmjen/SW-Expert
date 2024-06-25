from collections import deque

def process_queue_operations(test_cases):
    results = []
    for case_index, (queue_size, commands) in enumerate(test_cases):
        q = deque(maxlen=queue_size)  # 제한된 크기의 큐
        result = [f"#{case_index + 1}"]
        for command in commands:
            if command[0] == 1:
                if len(q) < queue_size:
                    q.appendleft(command[1])
            elif command[0] == 2:
                if len(q) < queue_size:
                    q.append(command[1])
            elif command[0] == 3:
                if q:
                    result.append(str(q[0]))
            elif command[0] == 4:
                if q:
                    result.append(str(q[-1]))
            elif command[0] == 5:
                if q:
                    q.popleft()
            elif command[0] == 6:
                if q:
                    q.pop()
        results.append(" ".join(result))
    
    return results

if __name__ == "__main__":
    input_file = 'input.txt'
    
    # 파일에서 입력 읽기
    with open(input_file, 'r') as file:
        data = file.read().strip().split('\n')
    
    test_case_count = int(data[0].strip())
    index = 1
    test_cases = []
    
    for _ in range(test_case_count):
        queue_size, command_count = map(int, data[index].strip().split())
        index += 1
        commands = []
        for i in range(command_count):
            command = list(map(int, data[index + i].strip().split()))
            commands.append(command)
        test_cases.append((queue_size, commands))
        index += command_count
    
    outputs = process_queue_operations(test_cases)
    for output in outputs:
        print(output)