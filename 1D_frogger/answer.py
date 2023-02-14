def main():
    input_list =[int(x) for x in input().split()]

    num_squares = input_list[0]
    frog_start = input_list[1] - 1 # Zero indexed
    magic_number = input_list[2]
    hops = 0
    visited = set()
    values = [int(x) for x in input().split()]

    frog_current = frog_start
    while True:
        if values[frog_current] == magic_number:
            return ["magic", hops]

        if frog_current in visited:
            return ["cycle", hops]
        visited.add(frog_current)
        
        if values[frog_current] >= 0:
            for i in range (values[frog_current]):
                if frog_current + 1 < num_squares:
                    frog_current+=1
                else:
                    return ["right", hops]

        else:
            for i in range (abs(values[frog_current])):
                if not frog_current - 1 < 0:
                    frog_current-=1
                else:
                    return ["left", hops]
        hops += 1

        
        
result = main()

print(result[0])
print(result[1])