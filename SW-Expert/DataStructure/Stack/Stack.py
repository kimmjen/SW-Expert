def process_stack_operations(test_cases):
    results = []
    for case_index, case in enumerate(test_cases):
        n, numbers = case
        stack = []
        for number in numbers:
            stack.append(number)
        
        reversed_numbers = []
        while stack:
            reversed_numbers.append(stack.pop())
        
        result = f"#{case_index + 1} " + " ".join(map(str, reversed_numbers))
        results.append(result)
    
    return results

if __name__ == "__main__":
    input_file = 'input.txt'
    
    with open(input_file, 'r') as file:
        data = file.read().strip().split()
    
    test_case_count = int(data[0])
    index = 1
    test_cases = []
    
    for _ in range(test_case_count):
        n = int(data[index])
        numbers = list(map(int, data[index + 1: index + 1 + n]))
        test_cases.append((n, numbers))
        index += n + 1
    
    outputs = process_stack_operations(test_cases)
    for output in outputs:
        print(output)