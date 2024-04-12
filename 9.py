a = int(input('Введите верхнюю границу диапазона:'))
for i in range(2, a + 1):
    b = False
    for j in range(2, i):
        if i % j == 0:
            b = True
            break
    if not b:
        print(i)
