def valid(result, operands):
    tmp = [operands[0]]
    
    for i in range(1, len(operands)):
        new_tmp = set()
        for v in tmp: 
            m, s = operands[i] * v, operands[i] + v
            
            if m <= result:
                new_tmp.add(m)
                
            if s <= result:
                new_tmp.add(s)
        
        tmp = new_tmp
        
    return result in new_tmp

def filter_valid_equation_results(results, operands):
    valid_equation_results = []
    for i, result in enumerate(results):
        if valid(result, operands[i]):
            valid_equation_results.append(result)
    return valid_equation_results

if __name__ == '__main__':
    results = []
    operands = []
    
    with open("./input.txt") as f:
        for line in f:
            result, values = line.split(":")
            results.append(int(result.strip()))
            operands.append([int(v.strip()) for v in values.split()])
            
    valid_equation_results = filter_valid_equation_results(results, operands)
            
    print(sum(valid_equation_results))