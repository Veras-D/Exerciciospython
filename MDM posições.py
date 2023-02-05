import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig = plt.figure()
ax = fig.add_subplot(111)
# identificar elos e juntas
a = float(input('Qual o comprimento da manivela (em milímetros)? '))
b = float(input('Qual o comprimento do da biela (em milímetros)? '))
c = float(input('Qual o comprimento do acilador (em milímetros)? '))
d = float(input('Qual o comprimento do eixo fixo (em milímetros)? '))


def animate(i):
    # Posição inicial
    o2 = [0, 0]
    o4 = [d, 0]
    theta_2 = math.radians(i)
    # Ponto A
    Ax = a * math.cos(theta_2)
    Ay = a * math.sin(theta_2)
    A = [Ax, Ay]
    # Valores auxiliares
    S = (a ** 2 - b ** 2 + c ** 2 - d ** 2) / (2 * (Ax - d))
    P = ((Ay ** 2) / (Ax - d) ** 2) + 1
    Q = (2 * Ay * (d - S)) / (Ax - d)
    R = (d - S) ** 2 - c ** 2
    # Ponto B
    By = (-Q + math.sqrt(Q ** 2 - 4 * P * R)) / (2 * P)
    By_l = (-Q - math.sqrt(Q ** 2 - 4 * P * R)) / (2 * P)
    Bx = S - ((Ay * By) / (Ax - d))
    Bx_l = S - ((2 * Ay * By_l) / (2 * (Ax - d)))
    B = [Bx, By]
    B_l = [Bx_l, By_l]
    # Ângulos
    theta_3 = math.atan((By - Ay) / (Bx - Ax))
    theta_4 = math.atan(By / (Bx - d))
    # Grafico
    x = [o2[0], A[0], B[0], o4[0]]
    y = [o2[1], A[1], B[1], o4[1]]
    ax.clear()
    ax.plot(x, y)


ani = animation.FuncAnimation(fig, animate, frames=360, interval=100)
plt.show()
# Ver até quantos grus a peça vai
