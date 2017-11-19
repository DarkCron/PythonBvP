def Sum(list):
    length = len(list)
    if length == 1:
        return list[0]

    return Sum(list[0:length-1]) + list[length-1]

print(Sum([2,9,3,6,2,5,3]))