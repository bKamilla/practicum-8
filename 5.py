a = int(input('Введите конец интервала:'))
result = 0
for i in range(2, a+1):
    summa = 0
    for j in range(1, i // 2 + i % 2 + 1):
        if i % j == 0:
            summa += j
    if summa == i:
        result += 1
print(result)