def swap_max(items: list) -> list:
    current_max  = 0
    index  = 0
    for i in range (len(items)):
        if current_max<=items[i]:
            current_max = items[i]
            index = i

    temp = items[0]
    items[0] = items[index]
    items[index] = temp

    return [items[0], items[index]]


if __name__ == "__ main__":
    numbers = [2,0,5,4,7,6,9,3,4,5]

    x = swap_max(numbers)

    print(x)
