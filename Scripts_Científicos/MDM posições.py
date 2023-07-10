import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig = plt.figure()
ax = fig.add_subplot(111)
# identificar elos e juntas
a = float(input('Qual o comprimento da manivela (em milímetros)? '))
b = float(input('Qual o comprimento do da acoplador (em milímetros)? '))
c = float(input('Qual o comprimento do acilador (em milímetros)? '))
d = float(input('Qual o comprimento do eixo fixo (em milímetros)? '))
delta_2 = math.radians(float(input('Qual o ângulo de defasagem do elo a em graus? ')))
delta_3 = math.radians(float(input('Qual o ângulo de defasagem do elo b em graus? ')))
delta_4 = math.radians(float(input('Qual o ângulo de defasagem do elo c em graus? ')))
s = float(input('Qual o modulo do vetor de defasagem S? '))
p = float(input('Qual o modulo do vetor de defasagem P? '))
u = float(input('Qual o modulo do vetor de defasagem U? '))
theta_2_lim_1 = ((a**2 - b**2 - c**2 + d**2) / (2 * a * d)) + ((b * c) / (a * d))
theta_2_lim_2 = ((a**2 - b**2 - c**2 + d**2) / (2 * a * d)) - ((b * c) / (a * d))
lista = [theta_2_lim_1, theta_2_lim_2]
lista = sorted(lista, reverse=True)
theta_2_min = math.degrees(lista[1])
theta_2_max = math.degrees(lista[0])
theta_2_range = range(math.floor(theta_2_min), math.ceil(theta_2_max))


# Posição inicial
def animate(i):
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
    rs = [s * math.cos(theta_2 + delta_2), s * math.sin(theta_2 + delta_2)]
    rp = [p * math.cos(theta_3 + delta_3) + A[0], p * math.sin(theta_3 + delta_3) + A[1]]
    ru = [u * math.cos(theta_4 + delta_4) + o4[0], u * math.sin(theta_4 + delta_4) + o4[1]]

    # Grafico
    x = [o2[0], A[0], B[0], o4[0]]
    y = [o2[1], A[1], B[1], o4[1]]
    x1 = [o2[0], rs[0], A[0]]
    y1 = [o2[1], rs[1], A[1]]
    x2 = [A[0], rp[0], B[0]]
    y2 = [A[1], rp[1], B[1]]
    x3 = [o4[0], ru[0], B[0]]
    y3 = [o4[1], ru[1], B[1]]
    ax.clear()
    ax.plot(x, y)
    ax.plot(x1, y1)
    ax.plot(x2, y2)
    ax.plot(x3, y3)


ani = animation.FuncAnimation(fig, animate, frames=theta_2_range, interval=100)
plt.show()
