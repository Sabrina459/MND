from functools import reduce
from random import randint
from math import sqrt
import numpy as np
from numpy.linalg import det
from prettytable import PrettyTable

def average(list):
    avrg = 0
    for element in list:
        avrg += element
    avrg = avrg / len(list)
    return avrg


def dispersion(list):
    list_average = average(list)
    dispersion = 0
    for element in list:
        dispersion += (element - list_average) ** 2 / len(list)
    return dispersion


def main():
    minX = [-20, -15, -15]
    maxX = [15, 35, -10]

    maxY = int(200 + average(maxX))
    minY = int(200 + average(minX))

    m = 3
    N = 2**(m-1)
    gener_x = []
    for i in range(N):
        gener_x.append([])
        gener_x[i].append(randint(minX[0], maxX[0]))
        gener_x[i].append(randint(minX[1], maxX[1]))
        gener_x[i].append(randint(minX[2], maxX[2]))

    plan_matrix = []
    for str_ind in range(N):
        plan_matrix.append([])
        plan_matrix[str_ind].append(1)
        for xi in gener_x[str_ind]:
            index = gener_x[str_ind].index(xi)
            if average([minX[index], maxX[index]])<xi:
                plan_matrix[str_ind].append(1)
            else:
                plan_matrix[str_ind].append(-1)
    #Матриця планування з натуралізованними значеннями факторів
    experement_matrix = []
    for i in range(len(plan_matrix)):
        experement_matrix.append([])
        for j in range(1, len(plan_matrix[i])):
            if plan_matrix[i][j]==1:
                experement_matrix[i].append(maxX[j-1])
            else:
                experement_matrix[i].append(minX[j - 1])
    gener_y=[]
    for i in range(N):
        gener_y.append([])
        gener_y[i].append(randint(minY, maxY))
        gener_y[i].append(randint(minY, maxY))
        gener_y[i].append(randint(minY, maxY))
    b = np.array(experement_matrix)
    Tgener_y = b.T
    avrg_y = []
    for i in range(len(gener_y)):
        avrg_y.append(average(gener_y[i]))

    # Математичне очікування
    a = np.array(experement_matrix)
    Texperement_matrix = a.T

    mx1 = reduce(lambda a, b: a + b, Texperement_matrix[0]) / 4
    mx2 = reduce(lambda a, b: a + b, Texperement_matrix[1]) / 4
    mx3 = reduce(lambda a, b: a + b, Texperement_matrix[2]) / 4
    my = reduce(lambda a, b: a + b, avrg_y) / 4

    a1 = sum([Texperement_matrix[0][i] * avrg_y[i] for i in range(4)]) / 4
    a2 = sum([Texperement_matrix[1][i] * avrg_y[i] for i in range(4)]) / 4
    a3 = sum([Texperement_matrix[2][i] * avrg_y[i] for i in range(4)]) / 4

    a11 = sum([i * i for i in Texperement_matrix[0]]) / 4
    a22 = sum([i * i for i in Texperement_matrix[1]]) / 4
    a33 = sum([i * i for i in Texperement_matrix[2]]) / 4

    a12 = sum([Texperement_matrix[0][i] * Texperement_matrix[1][i] for i in range(4)]) / 4
    a13 = sum([Texperement_matrix[1][i] * Texperement_matrix[2][i] for i in range(4)]) / 4
    a23 = sum([Texperement_matrix[2][i] * Texperement_matrix[0][i] for i in range(4)]) / 4
    a21 = a12
    a31 = a13
    a32 = a23


    b0 = det([[my, mx1, mx2, mx3],
              [a1, a11, a12, a13],
              [a2, a21, a22, a23],
              [a3, a31, a32, a33]]) / det([[1, mx1, mx2, mx3],
                                           [mx1, a11, a12, a13],
                                           [mx2, a21, a22, a23],
                                           [mx3, a31, a32, a33]])
    b1 = det([[1, my, mx2, mx3],
              [mx1, a1, a12, a13],
              [mx2, a2, a22, a23],
              [mx3, a3, a32, a33]]) / det([[1, mx1, mx2, mx3],
                                           [mx1, a11, a12, a13],
                                           [mx2, a21, a22, a23],
                                           [mx3, a31, a32, a33]])
    b2 = det([[1, mx1, my, mx3],
              [mx1, a11, a1, a13],
              [mx2, a21, a2, a23],
              [mx3, a31, a3, a33]]) / det([[1, mx1, mx2, mx3],
                                           [mx1, a11, a12, a13],
                                           [mx2, a21, a22, a23],
                                           [mx3, a31, a32, a33]])
    b3 = det([[1, mx1, mx2, my],
              [mx1, a11, a12, a1],
              [mx2, a21, a22, a2],
              [mx3, a31, a32, a3]]) / det([[1, mx1, mx2, mx3],
                                           [mx1, a11, a12, a13],
                                           [mx2, a21, a22, a23],
                                           [mx3, a31, a32, a33]])

    c = np.array(plan_matrix)
    Tplan_matrix = c.T
    plan_table = PrettyTable()
    plan_table.field_names = ['№','X0', 'X1', 'X2', 'X3', *[f"Y{i}" for i in range(1, N)]]
    for i in range(N):
        plan_table.add_row([i + 1, Tplan_matrix[0][i], Tplan_matrix[1][i], Tplan_matrix[2][i], Tplan_matrix[3][i], *gener_y[i]])
    print(plan_table)
    experement_table = PrettyTable()
    experement_table.field_names = ['№', 'X1', 'X2', 'X3', *[f"Y{i}" for i in range(1, N)]]
    for i in range(N):
        experement_table.add_row(
            [i + 1, *experement_matrix[i], *gener_y[i]])

    print(experement_table)
    print(avrg_y)
    print(f'y = {b0} + {b1}*x1 + {b2}*x2 + {b3}*x3')
    # dispersion_list = []
    # for i in range(N):
    #     dispersion_list.append(dispersion(gener_y[i]))
    for i in range(4):
        y = b0 + b1 * Texperement_matrix[0][i] + b2 * Texperement_matrix[1][i] + b3 * Texperement_matrix[2][i]
        print('y =', y)
    dispersion = [((gener_y[0][i] - avrg_y[i])**2  + (gener_y[1][i] - avrg_y[i])**2  + (gener_y[2][i] - avrg_y[i])**2 + (gener_y[3][i] - avrg_y[i])**2 ) / 4 for i in
                  range(3)]
    print('dispersion:', dispersion)

    gp = max(dispersion) / sum(dispersion)
    print('Gp =', gp)

    # Рівень значимості q = 0.05; f1 = m - 1 = 2; f2 = N = 4
    # За таблицею Gт = 0.7679
    if gp < 0.7679:
        print('Дисперсія однорідна')
    else:
        print('Дисперсія неоднорідна')
        exit()
    b_list = [b0, b1, b2, b3]
    # Оцінка значимості коефіцієнтів регресії згідно критерію Стьюдента
    s2b = sum(dispersion) / N
    s2bs_avg = s2b / (N * m)
    sb = s2bs_avg**(1/2)

    beta0 = sum([(avrg_y[i] * Tplan_matrix[0][i]) for i in range(4)]) / 4
    beta1 = sum([(avrg_y[i] * Tplan_matrix[1][i]) for i in range(4)]) / 4
    beta2 = sum([(avrg_y[i] * Tplan_matrix[2][i]) for i in range(4)]) / 4
    beta3 = sum([(avrg_y[i] * Tplan_matrix[3][i]) for i in range(4)]) / 4

    beta_arr = [beta0, beta1, beta2, beta3]
    t_arr = [abs(beta_arr[i]) / sb for i in range(4)]
    t_arr = [round(b_list[i]) for i in range(len(b_list))]

    # f3 = f1*f2 = 2*4 = 8
    # З таблиці беремо значення 2.306
    indexes = []
    unk_koef = []
    for i, v in enumerate(t_arr):
        if t_arr[i] > 2.306:
            indexes.append(i)
        else:
            unk_koef.append(i)
            print(f'Коефіцієнт b{i} = {b_list[i]} приймаємо не значним')
    ind = [i for i in range(N)]


    print(f'y = b{ind[0]}')

    b_res = [b_list[ind[0]] for _ in range(4)]
    for i in b_res:
        print(f'y = {i}')

    # Критерій Фішера
    # кількість значимих коефіцієнтів
    d = 1
    s2_ad = m * sum([(avrg_y[i] - b_res[i]) ** 2 for i in range(4)]) / 4 - d
    fp = s2_ad / s2b
    print(f'Fp = {fp}')

    # Fт = 4.5
    if fp > 4.5:
        print('Рівняння регресії неадекватно оригіналу при рівні значимості 0.05')
    else:
        print('Рівняння регресії адекватно оригіналу при рівні значимості 0.05')

    print('Таблиця незначних коефіцієнтів:')
    koef_table = PrettyTable()
    koef_table.field_names = [f'b{i}' for i in unk_koef]
    koef_table.add_row([b_list[i] for i in unk_koef])
    print(koef_table)


if __name__ == '__main__':
    main()
