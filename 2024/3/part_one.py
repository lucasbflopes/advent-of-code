import re

with open("./input.txt") as f:
    instructions = "".join(line.strip() for line in f)

print(sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", instructions)))
