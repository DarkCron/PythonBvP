def Maximum(list):
    length = len(list)-1
    if length == 0:
        return list[0]
    if list[0] < list[length]:
        return  Maximum(list[1:length+1])
    else:
        return Maximum(list[0:length])

print(Maximum([2,9,3,6,12,5,61]))