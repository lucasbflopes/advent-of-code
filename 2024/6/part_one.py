def up(i, j): return i-1, j
def down(i, j): return i+1, j
def right(i, j): return i, j+1
def left(i, j): return i, j-1

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
            
if __name__ == '__main__':
    with open("./input.txt") as f:
        data = [[c for c in line.strip()] for line in f]
        
    visited_positions = set()
    cur_x, cur_y = find_guard_position(data)
    guard = data[cur_x][cur_y]
    
    while (is_within_bounds(data, cur_x, cur_y)):
        next_x, next_y = direction(guard)(cur_x, cur_y)
        if not is_within_bounds(data, next_x, next_y):
            break
        
        if data[next_x][next_y] == "#":
            next_x, next_y = next_direction_90deg(guard)(cur_x, cur_y)
            if not is_within_bounds(data, next_x, next_y):
                break
            
            cur_x, cur_y = next_x, next_y
            guard = rotate_guard(guard)
            visited_positions.add((cur_x, cur_y))
        else:
            cur_x, cur_y = next_x, next_y
            visited_positions.add((cur_x, cur_y))

    print(len(visited_positions))

