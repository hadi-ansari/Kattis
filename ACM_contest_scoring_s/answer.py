logs = []
right_answers = []
while True:
    line = input()
    if line == "-1":
        break
    line = line.split()
    line[0] = int(line[0])
    logs.append(line)
    if line[2] == "right":
        right_answers.append(line[1])

final_score = 0

for problem in right_answers:
    problem_score = 0
    for log in logs:
        if log[1] == problem and log[2] == "wrong":
            problem_score += 20
        elif log[1] == problem and log[2] == "right":
            problem_score += log[0]
    final_score += problem_score

print('{} {}'.format(len(right_answers), final_score))