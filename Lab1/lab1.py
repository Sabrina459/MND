import random as ran
from prettytable import PrettyTable


def generate_rivnom(a, b):
    r = ran.random()
    return round(a + r * (b - a))


def main():
    a = 0
    b = 20
    x = PrettyTable()
    table = []
    a_0 = 1
    a_1 = 1
    a_2 = 1
    a_3 = 1
    X1 = list()
    X2 = list()
    X3 = list()
    Y = list()
    for i in range(8):
        X1.append(generate_rivnom(a, b))
        X2.append(generate_rivnom(a, b))
        X3.append(generate_rivnom(a, b))
        Y.append(a_0 + a_1 * X1[i] + a_2 * X2[i] + a_3 * X3[i])
        table.append(['' + format(i + 1), X1[i], X2[i], X3[i], Y[i]])
    x.field_names = ['', 'X1', 'X2', 'X3', 'Y']
    for i in range(len(table)):
        x.add_row(table[i])
    X01 = (max(X1) + min(X1)) / 2
    X02 = (max(X2) + min(X2)) / 2
    X03 = (max(X3) + min(X3)) / 2
    dX1 = X01 - min(X1)
    dX2 = X02 - min(X2)
    dX3 = X03 - min(X3)
    Xn1 = [(X1[i] - X01) / dX1 for i in range(8)]
    Xn2 = [(X2[i] - X02) / dX2 for i in range(8)]
    Xn3 = [(X3[i] - X03) / dX3 for i in range(8)]
    Yet = a_0 + a_1 * X01 + a_2 * X02 + a_3 * X03
    Xn1 = [round(el, 2) for el in Xn1]
    Xn2 = [round(el, 2) for el in Xn2]
    Xn3 = [round(el, 2) for el in Xn3]
    x.add_column('Xn1', Xn1)
    x.add_column('Xn2', Xn2)
    x.add_column('Xn3', Xn3)
    et = PrettyTable()
    et.field_names = ['Yet']
    et.add_row([Yet])
    maximum = PrettyTable()
    index = Y.index(max(Y))
    max_list = [X1[index], X2[index], X3[index]]
    maximum.field_names = ['', 'X1 X2 X3', 'Y']
    maximum.add_row(['max(Y):', max_list, max(Y)])
    print(x)
    print(et)
    print(maximum)


if __name__ == "__main__":
    main()
