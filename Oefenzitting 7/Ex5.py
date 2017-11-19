
def ruler(n):
    if n == 0:
        return
    for j in range(0,n):
        for i in range(0,n):
            print("-",end="")
        print()
        ruler(n-1)

    for i in range(0, n-1):
        print("-", end="")
    if (n - 1) > 0:
        print("-", end="")
        print()

ruler(4)