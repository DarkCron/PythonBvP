def cashier(amount, coins):
    if amount == 0:
        return 1

    total = 0
    tmp = 0
    for coin in coins:
        if coin != coins[0]:
            if amount%coin == 0:
                total+=1
        tmp += coin
    if tmp == amount:
        total+=1


    return cashier(amount - coins[0], coins) + total


print(cashier(13,[1,2,5]))