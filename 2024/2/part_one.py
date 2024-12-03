with open("./input.txt") as f:
    reports = [[int(v.strip()) for v in line.split()] for line in f]

result = 0
for report in reports:
    safe = True
    decreasing = report[0] > report[1]
    
    for a, b in zip(report, report[1:]):
        if not ((abs(b-a) >= 1 and abs(b-a) <=3) and (a > b if decreasing else b > a)):
            safe = False
            break
    
    if safe:
        result += 1
    
print(result)
