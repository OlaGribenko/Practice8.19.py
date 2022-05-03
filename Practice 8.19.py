Tickets = int(input('Введите количество билетов: '))
Sum = 0
for i in range(Tickets):
    age = int(input("Возраст посетителя: "))
    if age < 18:
        print('Вход бесплатный.')
    elif 18 <= age < 25:
        s = 990
        Sum = Sum + s
        print('К оплате: ', s)
    else:
        s = 1390
        print('К оплате: ', s)
        Sum = Sum + s
print('Всего к оплате:', Sum)
if Tickets > 3:
    f = 0.9
else:
    f = 1
print('Всего к оплате с учетом скидки', Sum * f)