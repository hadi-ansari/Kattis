num_stores = int(input())
num_items = int(input())

items = {}


for i in range(num_items):
    line = input().split()
    store_idx = int(line[0])
    item_name = line[1]
    if not item_name in items:
        items[item_name] = [store_idx]
    else:
        stores = list(items[item_name])
        stores.append(store_idx)
        items[item_name] = stores


purchased_items = int(input())
purchased_items_list = []

for i in range(purchased_items):
    purchased_items_list.append(input())

# print(items)
# print(purchased_items_list)
# print()

res = False

for store_idx in range(purchased_items):
    if store_idx not in items[purchased_items_list[store_idx]]:
        res = True
        print("impossible")
        break
    elif len(items[purchased_items_list[store_idx]]) > 1:
        res = True
        print("ambiguous")
        break

if not res:
    print("unique")

