SIZE = 4


board = []
for i in range(SIZE):
    line =[int(x) for x in input().split()]
    print(line)
    board.append(line)
move = int(input())
merged = set()

# LEFT
if move == 0:
    print("left")
    for y in range(SIZE):
        for x in range(SIZE):
            if x <= 0:
                continue
            temp_idx = x - 1
            while temp_idx >= 0:
                curr = board[y][temp_idx + 1]
                prev = board[y][temp_idx]
                if prev == 0:
                    board[y][temp_idx] = curr
                    board[y][temp_idx + 1] = 0
                elif prev == curr and not prev == 0 and (y, temp_idx) not in merged and (y, temp_idx + 1) not in merged:
                    board[y][temp_idx] *= 2
                    board[y][temp_idx + 1] = 0
                    merged.add((y, temp_idx))
                    break
                temp_idx -= 1

# UP            
elif move == 1:
    print("up")
    for y in range(SIZE):
        for x in range(SIZE):
            if y <= 0:
                break
            temp_idx = y - 1
            while temp_idx >= 0:
                curr = board[temp_idx + 1][x]
                prev = board[temp_idx][x]
                if prev == 0:
                    board[temp_idx][x] = curr
                    board[temp_idx + 1][x] = 0
                elif prev == curr and not prev == 0 and (temp_idx, x) not in merged and (temp_idx + 1, x) not in merged:
                    board[temp_idx][x] *= 2
                    board[temp_idx + 1][x] = 0
                    merged.add((temp_idx, x))
                    break
                temp_idx -= 1
# RIGHT
elif move == 2:
    print("right")
    for y in range(SIZE):
        for x in range(SIZE - 1, -1, -1):
            if x >= SIZE - 1:
                continue
            
            temp_idx = x + 1
            while temp_idx <= SIZE - 1:
                curr = board[y][temp_idx - 1]
                prev = board[y][temp_idx]
                if prev == 0:
                    board[y][temp_idx] = curr
                    board[y][temp_idx - 1] = 0
                elif prev == curr and not prev == 0 and (y, temp_idx) not in merged and (y, temp_idx - 1) not in merged:
                    board[y][temp_idx] *= 2
                    board[y][temp_idx - 1] = 0
                    merged.add((y, temp_idx))
                    break
                temp_idx += 1

# DOWN
elif move == 3:
    print("down")
    for y in range(SIZE - 1, -1, -1):
        for x in range(SIZE):
            if y <= 0:
                break
            temp_idx = y - 1
            while temp_idx >= 0:
                curr = board[temp_idx + 1][x]
                prev = board[temp_idx][x]
                if curr == 0:
                    board[temp_idx + 1][x] = prev
                    board[temp_idx][x] = 0
                elif prev == curr and not prev == 0 and (temp_idx, x) not in merged and (temp_idx + 1, x) not in merged:
                    board[temp_idx + 1][x] *= 2
                    board[temp_idx][x] = 0
                    merged.add((temp_idx + 1, x))
                    break
                temp_idx -= 1


print()
for row in board:
    print("{} {} {} {}".format(row[0], row[1], row[2], row[3]))

 