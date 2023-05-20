line =[int(x) for x in input().split()]
no_cheese_types = line[0]
offered_cheese_blends = line[1]


print('no_cheese_types is: {}\noffered_cheese_blends is: {}\n'.format(no_cheese_types, offered_cheese_blends))


cheese_on_hand = [int(x) for x in input().split()]
cheese_precentage = []
for i in range(0, offered_cheese_blends):
    cheese_precentage.append([float(x) for x in input().split()])

print('on-hand: {}\n'.format(cheese_on_hand))

for p in cheese_precentage:
    print(p)