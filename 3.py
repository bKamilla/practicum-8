m = float(input('Введите месячный доход:'))
summ = 0
k = 0
if m == 0:
    k = 1
while m != 0:
    summ += m
    k += 1
    m = float(input('Введите месячный доход:'))
m = summ / k
print(m)
