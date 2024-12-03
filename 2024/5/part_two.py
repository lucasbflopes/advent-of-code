from collections import defaultdict

with open("./input.txt") as f:
    lines = f.readlines()
    divider = lines.index("\n")
    
    rules = defaultdict(set)
    for i in range(divider):
        a, b = map(int, lines[i].strip().split("|"))
        rules[a].add(b)
        
    page_numbers = []
    for i in range(divider+1, len(lines)):
        page_numbers.append(list(map(int, lines[i].strip().split(","))))

invalid_page_numbers = []
for page_number in page_numbers:
    valid = True
    for i in reversed(range(len(page_number))):
        curr = page_number[i]
        others = set(page_number[:i])
        if len(rules[curr] & others) > 0:
            valid = False
            break
    if not valid:
        invalid_page_numbers.append(page_number)
        
for page_number in invalid_page_numbers:
    for i in range(len(page_number) - 1, 0, -1):
        while True:
            swaps = 0
            for j in range(i - 1, -1, -1):
                if page_number[j] in rules[page_number[i]]:
                    swaps += 1
                    page_number[i], page_number[j] = page_number[j], page_number[i]
            if swaps == 0:
                break
                
middle_total = 0
for page_number in invalid_page_numbers:
    middle_total += page_number[len(page_number)//2]

print(middle_total)