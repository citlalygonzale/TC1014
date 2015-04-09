def calculate_e(c):
    x = c
    ce = (1+1/x)**x
    return float(ce)

r = int(input("Number of decimal points of accuracy: "))

resulte = calculate_e(r)

print("The estimate of the constant e is:",resulte)
