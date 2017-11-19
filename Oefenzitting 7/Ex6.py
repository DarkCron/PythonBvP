def Pascal(x,y):
    if x==0:
        return 1;
    if x == y:
        return 1;
    if y == 0:
        return 1;
    return Pascal(x-1,y-1) + Pascal(x,y-1)

for i in range(0,10):
    for j in range(0,i+1):
        print(Pascal(j,i), end=" ")
    print()