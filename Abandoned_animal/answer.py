def find_path(purchased_items_list, num_stores, stores, path):
    for i in range(num_stores):
        while True:
            if len(purchased_items_list) > 0 and purchased_items_list[0] in stores[i]:
                purchase = dict()
                purchase["store"] = i
                purchase["item"] = purchased_items_list.pop(0)
                path.append(purchase)
            else:
                break

    if len(purchased_items_list) > 0:
        return False
    return True

def find_path2(purchased_items_list, num_stores, stores):
    for i in range(num_stores):
        while True:
            if len(purchased_items_list) > 0 and purchased_items_list[0] in stores[i]:
                purchased_items_list.pop(0)
            else:
                break

    if len(purchased_items_list) > 0:
        return False
    return True


def main():
    num_stores = int(input())
    num_items = int(input())

    stores = {}

    for i in range(num_items):
        line = input().split()
        store_idx = int(line[0])
        item_name = line[1]
        if not store_idx in stores:
            stores[store_idx] = [item_name]
        else:
            items_list = list(stores[store_idx])
            items_list.append(item_name)
            stores[store_idx] = items_list


    purchased_items = int(input())
    purchased_items_list = []

    for i in range(purchased_items):
        purchased_items_list.append(input())

    path = []
    temp_purchased_items_list = list(purchased_items_list)
    if not find_path(temp_purchased_items_list, num_stores, stores, path):
        return "impossible"

    # Finding out if the path is unique?
    for purchase in path:
        temp_stores = dict(stores)
        temp_purchased_items_list = list(purchased_items_list)
        temp_list = list(temp_stores[purchase["store"]])
        temp_list.remove(purchase["item"])
        temp_stores[purchase["store"]] = temp_list

        if find_path2(temp_purchased_items_list, num_stores, temp_stores):
            return "ambiguous"
       
    return "unique"

print(main())