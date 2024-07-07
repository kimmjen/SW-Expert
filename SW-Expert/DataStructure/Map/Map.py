def process_map_operations(test_cases):
    results = []
    for case_index, commands in enumerate(test_cases):
        result = [f"#{case_index + 1}"]
        map_dict = {}
        for command in commands:
            op_type = command[0]
            if op_type == 1:
                key, value = command[1:]
                map_dict[key] = value
            elif op_type == 2:
                key = command[1]
                if key in map_dict:
                    del map_dict[key]
            elif op_type == 3:
                key = command[1]
                if key in map_dict:
                    result.append(str(map_dict[key]))
                else:
                    result.append("-1")
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
            command = list(map(int, data[index + i].strip().split()))
            commands.append(command)
        test_cases.append(commands)
        index += command_count
    
    outputs = process_map_operations(test_cases)
    for output in outputs:
        print(output)