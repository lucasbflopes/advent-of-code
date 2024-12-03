def up(i, j): return i-1, j
def down(i, j): return i+1, j
def right(i, j): return i, j+1
def left(i, j): return i, j-1

def print_data(data):
    print("\n".join("".join(v for v in row) for row in data))
    print("\n")

def direction(guard):
    if guard == '^': return up
    if guard == '>': return right
    if guard == '<': return left
    if guard == 'v': return down
    
def next_direction_90deg(guard):
    if guard == '^': return right
    if guard == '>': return down
    if guard == '<': return up
    if guard == 'v': return left
    
def rotate_guard(guard):
    if guard == '^': return '>'
    if guard == '>': return 'v'
    if guard == '<': return '^'
    if guard == 'v': return '<'
    
def is_within_bounds(data, i, j):
    n, m = len(data), len(data[0])
    
    return 0 <= i < n and 0 <= j < m

def find_guard_position(data):
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value in '<>^v':
                return (i, j)
            
def found_loop(data):
    visited_positions = set()
    cur_x, cur_y = find_guard_position(data)
    guard = data[cur_x][cur_y]
    
    while (is_within_bounds(data, cur_x, cur_y)):
        next_x, next_y = direction(guard)(cur_x, cur_y)
        if not is_within_bounds(data, next_x, next_y):
            return False
        
        x, y = next_x, next_y
        while data[x][y] == "#":
            x, y = next_direction_90deg(guard)(cur_x, cur_y)
            guard = rotate_guard(guard)
            if not is_within_bounds(data, next_x, next_y):
                return False
        
        cur_x, cur_y = x, y
        if (cur_x, cur_y, guard) in visited_positions:
            return True
        visited_positions.add((cur_x, cur_y, guard))
        
    return False
            
if __name__ == '__main__':
    with open("./input.txt") as f:
        data = [[c for c in line.strip()] for line in f]
        
    result = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in ">^<v":
                continue
            
            data_copy = [row[:] for row in data]
            data_copy[i][j] = "#"
            if found_loop(data_copy):
                result += 1

    print(result)

