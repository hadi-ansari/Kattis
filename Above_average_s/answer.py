num_of_tests = int(input())


for i in range(num_of_tests):
    line = [int(x) for x in input().split()]
    num_of_people = line.pop(0)
    sum = 0
    for grade in line:
        sum += grade

    average = sum / num_of_people
    above_average = 0
    for grade in line:
        if grade > average:
            above_average += 1

    precentage = 0
    precentage = above_average / num_of_people * 100
    print('{:.3f}%'.format(precentage))
