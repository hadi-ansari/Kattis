import itertools

def main():
    num_stores = int(input())
    num_items = int(input())

    items = {}


    for i in range(num_items):
        line = input().split()
        store_idx = int(line[0])
        item_name = line[1]
        if not store_idx in items:
            items[store_idx] = [item_name]
        else:
            items_list = list(items[store_idx])
            items_list.append(item_name)
            items[store_idx] = items_list


    purchased_items = int(input())
    purchased_items_list = []

    for i in range(purchased_items):
        purchased_items_list.append(input())

    # print(items)
    # print(purchased_items_list)
    # print()

    temp = list(purchased_items_list)
    for i in range(num_stores):
        while True:
            if len(temp) > 0 and temp[0] in items[i]:
                # print("{} exists in {}".format(temp[0], i))
                temp.pop(0)
            else:
                break

    if len(temp) > 0:
        return "impossible"

    appearance = []
    for item in purchased_items_list:
        l = []
        for i in range(num_stores):
            if item in items[i]:
                l.append(i)
        appearance.append(l)

    combinations = list(itertools.product(*appearance))
    filtered = [c for c in combinations if all(c[i] <= c[i+1] for i in range(purchased_items - 1))]
    if len(filtered) > 1:
        return "ambiguous"

    return "unique"

print(main())