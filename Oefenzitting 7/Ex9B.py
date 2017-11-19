

def count_paths_amount(x,y):
    if x == 0 and y == 0 :
        return 1
    if x > 0:
        if y > 0:
            return count_paths_amount(x-1,y) + count_paths_amount(x,y-1)
        else:
            return count_paths_amount(x - 1, y)
    else:
        return count_paths_amount(x,y-1)

path = []
def count_paths(x,y):
    if x == 0 and y == 0 :
        path.append((x, y))
        print_set(path)
    if x > 0:
        if y > 0:
            copy = path[:]
            path.append((x,y))
            count_paths(x - 1, y)
            del path[:]
            for point in copy:
                path.append(point)
            path.append((x,y))
            count_paths(x, y-1)
        else:
            path.append((x, y))
            count_paths(x-1, y)
    elif y > 0:
        path.append((x, y))
        count_paths(x, y-1)


def print_set(pathToPrint):
    print("{",end="")
    for point in pathToPrint:
        print(point,end="")
    print("}", end="\n")
    path = set()
    return

print(count_paths_amount(3,3))
count_paths(3,3)