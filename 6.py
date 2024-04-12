a = int(input('Введите натуральное число:'))
b = ' '
c = '*'
for i in range(1,a+1):
    d = b*(a-i) + c*i
    print(d)
