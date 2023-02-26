line = [int(x) for x in input().split()]

num_of_potions = line[0]
drinking_time = line[1]
effect_duration_list = []


for i in range(num_of_potions):
    effect_duration_list.append(int(input()))


drinking_time_total = 0
for t in effect_duration_list:
    drinking_time_total += t

effect_duration_list.sort(reverse=True)
max_duration = effect_duration_list[0]
if max_duration > (num_of_potions * drinking_time) - drinking_time:
    print("YES")
else:
    print("NO")