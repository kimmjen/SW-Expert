def process_hash_operations(test_cases):
    results = []
    
    for case_index, (n, pairs, q, queries) in enumerate(test_cases):
        hash_table = {}
        
        # 해시 테이블에 데이터 삽입
        for key, data in pairs:
            hash_table[key] = data
        
        # 키 검색 및 결과 저장
        result = [f"#{case_index + 1}"]
        for query in queries:
            if query in hash_table:
                result.append(hash_table[query])
            else:
                result.append("not find")
        
        results.append("\n".join(result))
    
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
        pairs = []
        for i in range(n):
            # 각 줄에서 key와 data를 분리
            line = data[index + 1 + i]
            key, data_value = line.split(maxsplit=1)
            pairs.append((key, data_value))
        
        q = int(data[index + 1 + n])
        queries = []
        for i in range(q):
            queries.append(data[index + 2 + n + i])
        
        test_cases.append((n, pairs, q, queries))
        index += 2 + n + q
    
    # 해시 테이블 연산 수행 및 결과 출력
    outputs = process_hash_operations(test_cases)
    for output in outputs:
        print(output)