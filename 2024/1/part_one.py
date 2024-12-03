l1, l2 = [], []
with open("./input.txt") as f:
    for line in f:            
        v1, v2 = line.split()
        l1.append(int(v1.strip()))
        l2.append(int(v2.strip()))

result = 0
for v1, v2 in zip(sorted(l1), sorted(l2)):
    result += abs(v1-v2)
    
print(result)
