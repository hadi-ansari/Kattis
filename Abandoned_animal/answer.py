def find_path(purchased_items_list, num_stores, items, path = False):
    for i in range(num_stores):
        while True:
            if len(purchased_items_list) > 0 and i in items[purchased_items_list[0]]:
                if not path == False:
                    purchase = dict()
                    purchase["store"] = i
                    purchase["item"] = purchased_items_list.pop(0)
                    path.append(purchase)
                else:
                    purchased_items_list.pop(0)
            else:
                break

    if len(purchased_items_list) > 0:
        return False
    return True

def main():
    num_stores = int(input())
    num_items = int(input())

    items = {}

    for i in range(num_items):
        line = input().split()
        store_idx = int(line[0])
        item_name = line[1]
        if not item_name in items:
            items[item_name] = {store_idx}
        else:
            items[item_name].add(store_idx)


    purchased_items = int(input())
    purchased_items_list = []

    for i in range(purchased_items):
        purchased_items_list.append(input())

    path = []

    temp_purchased_items_list = list(purchased_items_list)
    if not find_path(temp_purchased_items_list, num_stores, items, path):
        return "impossible"
    # Finding out if the path is unique?
    for purchase in path:
        temp_purchased_items_list = list(purchased_items_list)
        temp_items = {item: set(stores) - {purchase["store"]} for item, stores in items.items()}

        if find_path(temp_purchased_items_list, num_stores, temp_items):
            return "ambiguous"
       
    return "unique"

print(main())