class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.nodes = {}

    def insert(self, parent, child):
        if parent not in self.nodes:
            self.nodes[parent] = TreeNode(parent)
        if child not in self.nodes:
            self.nodes[child] = TreeNode(child)
        
        parent_node = self.nodes[parent]
        if parent_node.left is None:
            parent_node.left = self.nodes[child]
        else:
            parent_node.right = self.nodes[child]

    def pre_order_traversal(self, node, visit):
        if node:
            visit.append(node.value)
            self.pre_order_traversal(node.left, visit)
            self.pre_order_traversal(node.right, visit)

def process_tree_operations(test_cases):
    results = []
    for case_index, (node_num, edge_num, edges) in enumerate(test_cases):
        tree = BinaryTree()
        for i in range(0, len(edges), 2):
            parent = edges[i]
            child = edges[i + 1]
            tree.insert(parent, child)
        
        visit = []
        tree.pre_order_traversal(tree.nodes[1], visit)  # assuming the root is always node 1
        results.append(f"#{case_index + 1} " + " ".join(map(str, visit)))
    
    return results

if __name__ == "__main__":
    input_file = 'input.txt'
    
    # 파일에서 입력 읽기
    with open(input_file, 'r') as file:
        data = file.read().strip().split('\n')
    
    test_case_count = int(data[0].strip())
    index = 1
    test_cases = []
    
    # 테스트 케이스 처리
    for _ in range(test_case_count):
        node_num, edge_num = map(int, data[index].strip().split())
        edges = list(map(int, data[index + 1].strip().split()))
        test_cases.append((node_num, edge_num, edges))
        index += 2
    
    # 트리 연산 수행 및 결과 출력
    outputs = process_tree_operations(test_cases)
    for output in outputs:
        print(output)