BINARY = "binary"
DECIMAL = "decimal"
NEITHER = "neither"

def neighbors(graph, location, c):
    neighbors = []
    x = int(location[0]) + 1
    y = int(location[1])

    if y in graph and x > 0 and x <= c:
        neighbors.append((x, y))

    x = int(location[0]) - 1
    y = int(location[1])
    if y in graph and x > 0 and x <= c:
        neighbors.append((x, y))

    x = int(location[0])
    y = int(location[1]) - 1
    if y in graph:
        neighbors.append((x, y))

    x = int(location[0])
    y = int(location[1]) + 1
    if y in graph:
        neighbors.append((x, y))

    return neighbors


def find_path(graph, start, dest, mode, c):
    
    current = start
    q = []
    q.insert(0, current)
    visited = set()
    while len(q) > 0:
        current = q.pop()
        if current == dest and mode == DECIMAL and graph[current[1]][current[0] - 1] == 1:
            return True
        if current == dest and mode == BINARY and graph[current[1]][current[0] - 1] == 0:
            return True
        for n in neighbors(graph, current, c):
            if n not in visited and mode == DECIMAL and graph[n[1]][n[0] - 1] == 1:
                visited.add(n)
                q.insert(0, n)

            elif n not in visited and mode == BINARY and graph[n[1]][n[0] - 1] == 0:
                visited.add(n)
                q.insert(0, n)

    return False


def main():
    first = input().split()
    r = int(first[0])
    c = int(first[1])

    graph = {}
    for i in range(1, r + 1):
        graph[i] = [int(x) for x in list(input())]

    # print(graph)
    n = int(input())

    for i in range(n):
        question = [int(x) for x in input().split()]
        start = question[:2]
        dest = question[2:]
        start.reverse()
        dest.reverse()
        start = tuple(start)
        dest = tuple(dest)
        # print("start: {},\tdest: {}, mode: {}".format(start, dest, "binary"))
        if find_path(graph, start, dest, DECIMAL, c):
            print(DECIMAL)
        elif find_path(graph, start, dest, BINARY, c):
            print(BINARY)
        else:
            print(NEITHER)



main()