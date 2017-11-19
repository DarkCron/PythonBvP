def count_paths(x,y):
    if x == 0 and y == 0 :
        return 1
    if x > 0:
        if y > 0:
            return count_paths(x-1,y) + count_paths(x,y-1)
        else:
            return count_paths(x - 1, y)
    else:
        return count_paths(x,y-1)

print(count_paths(2,1))