def find_threes(l):
    sum = 0
    for c in l:
        if(c % 3 == 0):
            sum = sum + c
    return sum

n = [0,3,5,8,9,11,12,24]
print(find_threes(n))
