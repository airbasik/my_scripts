# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 13:49:55 2019

@author: Us
"""
import math
import time
#import numpy as np
import matplotlib.pyplot as plt


wingspan = 40
wing_area = 330

M_cruise = 0.8
oC = 0.15
mass_middle = 80000
g = 9.81
ro_h = 0.3648
a_h = 295

b_central = 5
b_end = 1
angle_sweep_LE = 27
angle_sweep_025 = 23
S_go = 21
S_vo = 19
area_middle_fus = 30
l_fus = 25
l_nose = 10
l_tail = 10
lenght_engine = 5
area_middle_engine = 2.5

oC_GO = 0.09
angle_sweep_025_GO = 30

oC_VO = 0.09
angle_sweep_025_VO = 40

d_fus_ef = (4*area_middle_fus/math.pi)**0.5
lya_fus = l_fus/d_fus_ef
lya_nose = l_nose/d_fus_ef
lya_tail = l_tail/d_fus_ef
l_centr = l_fus - l_nose - l_tail




def lengthening_wing(): #Удлинение крыла
    lya = wingspan**2/wing_area
    return(lya)
    
def narrowing():       #Сужение
    eta = b_central/b_end
    return(eta)

def Middle_Aerodynamic_Chord(): #Middle Aerodynamic Chord - Средняя аэродинамическая хорда
    print('Способы нахождения САХ крыла: \n1 - Формула \n2 - Геометрически')
    variable = input('Способ нахождения САХ: ')
#    variable = 1
    if variable in (1, '1', 'да', 'Формула', 'формула'):
        MAC = 2/3*(b_central + b_end - b_central*b_end/(b_central + b_end))
    elif variable in ('нет', '2', 'геом', 'геометрически', 'Геометрически'):
        try:    
            MAC = float(input('Введите длинну САХ, м: '))
        except ValueError:
            print('\033[1;31mНекорректный ввод. По умолчанию используется формула!\033[1;0m')
            MAC = 2/3*(b_central + b_end - b_central*b_end/(b_central + b_end))
    else:
        print('\033[1;31mНекорректный ввод. По умолчанию используется формула!\033[1;0m')
        MAC = 2/3*(b_central + b_end - b_central*b_end/(b_central + b_end))
    return(MAC)

def origin_MAC(): #координата Х САХ крыла
    x_cax = (b_central + 2*b_end)/(b_central + b_end)*wingspan/6*math.tan(angle_sweep_LE*math.pi/180)
    return(x_cax)
    
def o_area_GT(): #относительня площадь горизонтального оперения 
    oS_go = S_go/wing_area
    return(oS_go)

def o_area_VT(): #относительная площадь Вертикального оперения 
    oS_vo = S_vo/wing_area
    return(oS_vo)
    
def area_fuselage_washing(): #Омываемая площадь Фюзеляжа
        
    if l_centr < 0:
        print('\033[1;31mНеккоректный ввод значений длины фюзеляжа!')
        S_omuv = 0
        print('Дальнейший расчёт неверен. Проверьте длину фюзелажа на отрицательный результат!\033[1;0m')
    elif lya_fus >= 4.5 and l_centr > 0:
        S_omuv = math.pi*d_fus_ef*l_fus*(1 - 2/lya_fus)**(2/3)*(1+1/lya_fus**2)
    else:
        S_omuv = math.pi*d_fus_ef*l_fus*(0.5 + 0.135*lya_nose/lya_fus)**(2/3)*(1.015 + 0.3/lya_fus**1.5)
    return(S_omuv)
    
def area_engine_washing(): #Омываемая площадь двигателя
    print('Способы нахождения омываемой площади мотогондолы: \n1 - Упрощённый \n2 - Детальный')
    variable = input('Введите номер способа: ')
#    variable = 1
    if variable in (1, '1'):
        S_MG = 2.85*lenght_engine*(area_middle_engine)**0.5
    elif variable in (2, '2'):
        print('Введите парметры обтекателя вентилятора:')
        l_fan = float(input('Длина обтекателя вентилятора: '))
        D_fan = float(input('Диаметр обтекателя вентилятора в мидолевом сечении: '))
        D_obech = float(input('Диаметр носовой части обтекателя вентилятора: '))
        D_c_fan = float(input('Диаметр концевой части обтекателя вентилятора: '))
        l_fan_middle = float(input('Расстояние от носовой части обтекателя вентилятора до мидолевого сечения:'))
        beta = l_fan_middle/l_fan
        
        F_wash_fan = l_fan*D_fan*(2 + 0.35*beta + 0.8*beta*D_obech/D_fan + 1.15*(1 - beta)*D_c_fan/D_fan)

        print('Введите парметры газогенератора: ')
        l_gas = float(input('Длина газогенератора: '))
        D_gas = float(input('Диаметр газогенератора: '))
        D_c_gas = float(input('Диаметр концевой части газогенератора: '))
        
        F_was_gas = math.pi*l_gas*D_gas*(1 - 1/3*(1 - D_c_gas/D_gas)*(1 - 0.18*(D_gas/l_gas)**5/3))
        
        print('Введите парметры центрального тела:')
        l_ct = float(input('Длина центрального тела: '))
        D_ct = float(input('Диаметр центрального тела: '))
        
        F_wash_ct = 0.7*math.pi*l_ct*D_ct
        
        S_MG = F_wash_fan +F_was_gas + F_wash_ct
    else:
        print('Некорректный ввод. По умолчанию используется упрощённая формула!')
        S_MG = 2.85*lenght_engine*(area_middle_engine)**0.5
    return(S_MG)
    
def M_critical_wing():
    try:
        print('Тип профиля: \n1 - Обычный \n2 - Скоростной, пиковый \n3 - Суперкритический')
        K_nomer_profile = int(input('Введите тип профиля: '))
        alist = (1.0, 1.05, 1.15)
        K_type_profile = alist[K_nomer_profile-1]
#        print(K_type_profile)
        time.sleep(1)
    except:
        print('\033[1;31mНеккоректный ввод данных! Применяется обычный профиль\033[1;0m')
        K_type_profile = 1.0
    iteration = 5000
    Mcrit = M_cruise
    x_iter = [] #создание массивов для постороения графика 
    y_Mcrit = []
    for i in range(iteration):
        Cya = 2*mass_middle*g/ro_h/a_h**2/Mcrit**2/wing_area
        M_K = K_type_profile - 0.25*Cya/math.cos(angle_sweep_025*math.pi/180)
        oC1 = 0.3/Mcrit*(1/Mcrit/math.cos(angle_sweep_025*math.pi/180) - Mcrit*math.cos(angle_sweep_025*math.pi/180))**(1/3)*(1 - ((5 + ((Mcrit*math.cos(angle_sweep_025*math.pi/180))**2))/(5 + M_K**2))**3.5)**(2/3)
        oC1 = round(oC1, 5)
#        print('Итерация =', i, '\tCya =', Cya,'\tМкрит =', Mcrit, '\toC1 =', oC1)
        if oC-0.0001 < oC1 < oC+0.0001:
            break
        elif oC1 > oC:
            Mcrit += 0.0001
        else:
            Mcrit -= 0.0001
        x_iter.append(i) #добавление значений в массив для построения графиков
        y_Mcrit.append(Mcrit)
    print('Итерация =', i)
    plt.plot(x_iter,y_Mcrit) #координаты для графика
    ax = plt.subplot()
#    ax.set_title('Title')
    ax.set_xlabel('Итерация') #оси графика
    ax.set_ylabel('Число Маха')
    plt.show()  #показываем график
    Mcrit = round(Mcrit, 3)
    return(Mcrit)

def M_critical_fuselage():
    try:
        print('Форма носовой части: \n1 - Элептическая \n2 - Параболическая')
        type_nose_part = int(input('Введите тип носовой части: '))
        if type_nose_part == 1:
            Mcritfuz = 0.766 + 0.306 * math.log10(lya_nose)
        elif type_nose_part == 2:
            Mcritfuz = 0.806 + 0.254 * math.log10(lya_nose)
        else:
            print('\033[1;31mОшибка. Применяется формула для элептической носовой части\033[1;0m')
            Mcritfuz = 0.766 + 0.306 * math.log10(lya_nose)       
    except:
         print('\033[1;31mНеккоректный ввод данных! Применяется формула для элептической носовой части!\033[1;0m')
         Mcritfuz = 0.766 + 0.306 * math.log10(lya_nose)
    return(Mcritfuz)
    
def M_critical_GO():   
    iteration = 5000
    Mcrit = M_cruise
    for i in range(iteration):
        oC1 = 0.3/Mcrit*(1/Mcrit/math.cos(angle_sweep_025_GO*math.pi/180) - Mcrit*math.cos(angle_sweep_025_GO*math.pi/180))**(1/3)*(1 - ((5 + ((Mcrit*math.cos(angle_sweep_025_GO*math.pi/180))**2))/(5 + 1**2))**3.5)**(2/3)
        oC1 = round(oC1, 5)
#        print('Итерация =', i, '\tМкрит =', Mcrit, '\toC1 =', oC1)
        if oC_GO - 0.0001 < oC1 < oC_GO + 0.0001:
            break
        elif oC1 > oC_GO:
            Mcrit += 0.0001
        else:
            Mcrit -= 0.0001
    Mcrit = round(Mcrit, 3)
    return(Mcrit)
    
def M_critical_VO():   
    iteration = 5000
    Mcrit = M_cruise
    for i in range(iteration):
        oC1 = 0.3/Mcrit*(1/Mcrit/math.cos(angle_sweep_025_VO*math.pi/180) - Mcrit*math.cos(angle_sweep_025_VO*math.pi/180))**(1/3)*(1 - ((5 + ((Mcrit*math.cos(angle_sweep_025_GO*math.pi/180))**2))/(5 + 1**2))**3.5)**(2/3)
        oC1 = round(oC1, 5)
#        print('Итерация =', i, '\tМкрит =', Mcrit, '\toC1 =', oC1)
        if oC_VO - 0.0001 < oC1 < oC_VO + 0.0001:
            break
        elif oC1 > oC_GO:
            Mcrit += 0.0001
        else:
            Mcrit -= 0.0001
    Mcrit = round(Mcrit, 3)
    return(Mcrit)
    
def M_critical_min():
    Mcrit = [M_critical_wing(), M_critical_fuselage(), M_critical_GO(), M_critical_VO()]
    Mcrit.sort()
    return(Mcrit[0])

#def Speed_design(): #для турбореактивного самолёта
    
    


print('Критическое число маха самолёта:', M_critical_min())
      
    

#print('Удлинение:', lengthening_wing())
#print('Сужение:', narrowing())
#print('САХ:', Middle_Aerodynamic_Chord())
#print('Координата начала САХ:', origin_MAC())
#print('Относительная площадь ГО:', o_area_GT())
#print('Относительная площадь ВО:', o_area_VT())
#print('Омываемая площадь фюзеляжа:', area_fuselage_washing())
#print('Эквивалентный диаметр фюзеляжа:', d_fus_ef)
#print('Омываемая площать мотогондолы:', area_engine_washing())
#print('Критическое число маха:', M_critical_wing())  
#print('Критическое число маха фюзеляжа:', M_critical_fuselage())      
#print('Критическое число маха горизонтального оперения:', M_critical_GO())
#print('Критическое число маха вертикального оперения:', M_critical_VO())
















