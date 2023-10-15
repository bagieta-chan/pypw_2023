def swap_max(items: list) -> list:
    max_pos = items.index(max(items))
    items[0], items[max_pos] = items[max_pos], items[0]

    return items

numbers = [2,0,5,4,7,6,9,3,4,5]
print(swap_max(numbers))

