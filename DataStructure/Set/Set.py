def process_set_operations(test_cases):
    results = []
    for case_index, commands in enumerate(test_cases):
        result = [f"#{case_index + 1}"]
        my_set = set()
        for command in commands:
            op_type = command[0]
            value = command[1]
            if op_type == 1:
                my_set.add(value)
            elif op_type == 2:
                if value in my_set:
                    my_set.remove(value)
        sorted_elements = sorted(my_set)
        result.extend(map(str, sorted_elements))
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
        command_count = int(data[index].strip())
        index += 1
        commands = []
        for i in range(command_count):
            if index < len(data):
                command = list(map(int, data[index].strip().split()))
                commands.append(command)
                index += 1
        test_cases.append(commands)
    
    outputs = process_set_operations(test_cases)
    for output in outputs:
        print(output)