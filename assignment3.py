def ComputeList(list):
    return sum(list)

def ProductList(list):
    if len(list) == 0:
            return 0
    total = 1
    for i in list:
        total = total * list[i]
    return total

