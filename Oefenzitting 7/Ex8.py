# def cashier(amount, coins):
#     if amount == 0:
#         return 1
#
#     total = 0
#     tmp = 0
#     for coin in coins:
#         if coin != coins[0]:
#             if amount%coin == 0:
#                 total+=1
#         tmp += coin
#     if tmp == amount:
#         total+=1
#
#
#     return cashier(amount - coins[0], coins) + total

def cashier(amount, coins):
    if len(coins) == 0:
        return 0
    if amount == 0:
        return 1

    total = 0
    for i in range(1, len(coins)):
        if amount % coins[i] == 0:
            if len(coins) > 2:
                new_coins = [coins[0],coins[i]]
                total += cashier(amount - coins[0], new_coins)
            else:
                total += 1

    return total  + cashier(amount - coins[0], coins)


print(cashier(6, [1, 2, 5]))
