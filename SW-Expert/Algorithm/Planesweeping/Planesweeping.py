def calculate_area(rectangles):
    events = []
    for x1, y1, x2, y2 in rectangles:
        events.append((x1, y1, y2, 1))  # Rectangle start
        events.append((x2, y1, y2, -1)) # Rectangle end
    
    events.sort()
    
    active_intervals = []
    last_x = 0
    total_area = 0

    def compute_active_length():
        if not active_intervals:
            return 0
        active_intervals.sort()
        current_y1, current_y2 = active_intervals[0]
        total_length = 0
        for y1, y2 in active_intervals:
            if y2 <= current_y2:
                continue
            if y1 > current_y2:
                total_length += current_y2 - current_y1
                current_y1, current_y2 = y1, y2
            else:
                current_y2 = max(current_y2, y2)
        total_length += current_y2 - current_y1
        return total_length

    for x, y1, y2, typ in events:
        total_area += compute_active_length() * (x - last_x)
        if typ == 1:
            active_intervals.append((y1, y2))
        else:
            active_intervals.remove((y1, y2))
        last_x = x

    return total_area

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for t in range(T):
        N = int(data[idx])
        idx += 1
        rectangles = []
        for _ in range(N):
            x1 = int(data[idx])
            y1 = int(data[idx + 1])
            x2 = int(data[idx + 2])
            y2 = int(data[idx + 3])
            idx += 4
            rectangles.append((x1, y1, x2, y2))
        
        area = calculate_area(rectangles)
        results.append(f"#{t + 1} {area}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()