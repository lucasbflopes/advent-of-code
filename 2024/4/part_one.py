def up(i, j):         return i-1, j
def down(i, j):       return i+1, j
def right(i, j):      return i, j+1
def left(i, j):       return i, j-1
def up_right(i, j):   return i-1, j+1
def up_left(i, j):    return i-1, j-1
def down_right(i, j): return i+1, j+1
def down_left(i, j):  return i+1, j-1

def find_word_recur(data, i, j, found, target, direction):
    if (i < 0 or i == len(data)) or (j < 0 or j == len(data[i])): 
        return 0
    
    v = data[i][j]

    if found + v == target:
        return 1
    
    left_to_find = target.lstrip(found)

    if v != left_to_find[0]: 
        return 0
    
    new_i, new_j = direction(i, j)

    return find_word_recur(data, new_i, new_j, found + v, target, direction)

def find_word(data, i, j):
    found, target  = "", "XMAS"
    return (
        find_word_recur(data, i, j, found, target, up) +
        find_word_recur(data, i, j, found, target, down) +
        find_word_recur(data, i, j, found, target, right) +
        find_word_recur(data, i, j, found, target, left) +
        find_word_recur(data, i, j, found, target, up_left) +
        find_word_recur(data, i, j, found, target, up_right) +
        find_word_recur(data, i, j, found, target, down_right) +
        find_word_recur(data, i, j, found, target, down_left)
    )

with open("./input.txt") as f:
    data = [[c for c in line.strip()] for line in f]

found = 0
for i, row in enumerate(data):
    for j, _ in enumerate(row):
        found += find_word(data, i, j)

print(found)
