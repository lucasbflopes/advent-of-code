l1, c2 = [], {}
with open("./input.txt") as f:
    for line in f:            
        v1, v2 = [int(v.strip()) for v in line.split()]
        l1.append(v1)
        c2[v2] = c2.get(v2, 0) + 1

result = 0
for v1 in l1:
    result += v1 * c2.get(v1, 0)
    
print(result)
