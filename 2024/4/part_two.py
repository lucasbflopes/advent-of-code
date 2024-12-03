def up(i, j):         return i-1, j
def down(i, j):       return i+1, j
def right(i, j):      return i, j+1
def left(i, j):       return i, j-1
def up_right(i, j):   return i-1, j+1
def up_left(i, j):    return i-1, j-1
def down_right(i, j): return i+1, j+1
def down_left(i, j):  return i+1, j-1

def get_value(data, coord):
    i, j = coord
    
    if (i < 0 or i == len(data)) or (j < 0 or j == len(data[i])): 
        return None
    
    return data[i][j]

def find_word(data, i, j):
    if (get_value(data, (i, j)) == "A" and
        {get_value(data, up_right(i, j)), get_value(data, down_left(i, j))} == {"M", "S"} and
        {get_value(data, up_left(i, j)), get_value(data, down_right(i, j))} == {"M", "S"}):
        return 1
    else:
        return 0

with open("./input.txt") as f:
    data = [[c for c in line.strip()] for line in f]

found = 0
for i, row in enumerate(data):
    for j, _ in enumerate(row):
        found += find_word(data, i, j)

print(found)
