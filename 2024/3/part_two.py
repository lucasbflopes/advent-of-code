import re

with open("./input.txt") as f:
    instructions = "".join(line.strip() for line in f)

head, *others = instructions.split("don't")
instructions_to_consider = [head]
for other in others:
    _, *valid = other.split("do()")
    instructions_to_consider.extend(valid)

print(sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", "".join(instructions_to_consider))))
