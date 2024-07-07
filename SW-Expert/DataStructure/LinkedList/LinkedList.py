class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_all(self, value):
        count = 0
        dummy = ListNode(0)
        dummy.next = self.head
        current = dummy
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                count += 1
            else:
                current = current.next
        self.head = dummy.next
        return count

def process_linked_list_operations(test_cases):
    results = []
    for case_index, (N, operations) in enumerate(test_cases):
        linked_list = LinkedList()
        result = [f"#{case_index + 1}"]
        for operation in operations:
            mode, number = operation
            if mode == 1:
                linked_list.append(number)
            elif mode == 2:
                count = linked_list.delete_all(number)
                result.append(str(count))
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
        N = int(data[index].strip())
        operations = []
        for i in range(1, N + 1):
            mode, number = map(int, data[index + i].strip().split())
            operations.append((mode, number))
        test_cases.append((N, operations))
        index += N + 1
    
    outputs = process_linked_list_operations(test_cases)
    for output in outputs:
        print(output)