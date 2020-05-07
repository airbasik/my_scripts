# -*- coding: utf-8 -*-

import math

Mkp = 0.7
Xi = 2  # угол стреловидности по 1/4 хорды в градусах
K = 1  # зависит от типа профиля
mcp = 5701  # среняя крейсерская масса полёта
ro = 0.08890993456720298  # плотность воздуха на высоте
ah = 295  # скорость звука на высоте полёта
S = 66.1  # площадь крыла
a1, a2 = (0.14999, 0.15001)  # интервал для относительной толщины, !!!НЕ БОЛЬШЕ 4 ЗНАКОВ ПОСЛЕ ЗАПЯТОЙ!!!
xi = Xi / 180 * math.pi  # перевод в радианы
th = 5000

i = 0
while i < th:
    if th > i:
        Cya = round(2 * mcp * 9.81 / ro / ah ** 2 / Mkp ** 2 / S, 3)
        #    print('Cya =', Cya)
        Mi = round(K - 0.25 * Cya / (math.cos(xi)) ** 2, 3)
        #    print('Mi =', Mi)
        oc = round(0.3 / Mkp * (1 / Mkp / math.cos(xi) - Mkp * math.cos(xi)) ** (1 / 3) * (
                    1 - ((5 + ((Mkp * math.cos(xi)) ** 2)) / (5 + Mi ** 2)) ** 3.5) ** (2 / 3), 5)
        if a1 < oc < a2:
            print('oc =', round(oc, 2))
            print('Mkp =', round(Mkp, 3))
            print('Cya =', Cya)
            print('Mi =', Mi)
            break
            print('Критическое число маха посчитано')
        else:
            if oc < 0.15:
                Mkp -= 0.0001
            else:
                Mkp += 0.0001
            i = th - 1
    else:
        print('oc =', round(oc, 2))
        print('Mkp =', round(Mkp, 3))
        print('Cya =', Cya)
        print('Mi =', Mi)
        print('Ошибка, перезадай параметры')
        break
a = int(input('Нажми enter, что бы закрыть программу'))

#
