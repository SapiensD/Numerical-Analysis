import numpy as np
import matplotlib.pyplot as plt
## INPUT
a = list()  # иксы
b = list()  # игрики
inp = open("src/in.txt", "r")
n = int(inp.readline())
for i in range(n):
    a.append(float(inp.readline()))
for i in range(n):
    b.append(float(inp.readline()))
x = np.array(a, dtype=float) # массив узлов интерполяции
y = np.array(b, dtype=float)
inp.close()
limit = 1e-8
"""
## просто красиво
def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i != j:
                p1 *= (t - x[i])
                p2 *= (x[j] - x[i])
        z += y[j] * p1 / p2
    return z
"""
#   L:
#       L01
#       L12     L012
#       L23     L123    L0123
#       L34     L234    L1234   L01234
#       L45     L345    L2345   L12345  *L012345*
#

amount = 100
xnew = np.linspace(np.min(x), np.max(x), amount) # разбивает отрезок от мин(х) до макс(х) на AMOUNT отрезков
ynew = [0] * amount
for u in range(0, amount):
    P=[0]*n
    for i in range(n):
        P[i] = [0]*n

    P[0]=y
    for j in range(n-1):
        f = 0
        for i in range(j+1, n):
            P[j+1][i] = ( P[j][i]*(xnew[u]-x[j]) - P[j][j]*(xnew[u]-x[i]) )/(x[i]-x[j])
    ynew[u] = P[n-1][n-1]

# визуализация, можно пользоваться библиотеокй
plt.plot(x, y, 'o', xnew, ynew)
plt.grid(True)
plt.show()      # отображает точки с линиями

#   OUTPUT
out = open("src/out.txt", "w")
for i in range(amount):
    out.writelines(str(xnew[i]) + str(" ") + str(ynew[i]) + str('\n'))
out.close()