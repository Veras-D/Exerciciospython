import sympy as sp
x = sp.symbols('x')
xi = [600, 800, 1000, 1200, 1400, 1600]
y = [71720, 94720, 118400, 142080, 165760, 189440]
h = xi[1] - xi[0]
z = (x - xi[0]) / h
delta = [y[0]]
delta1 = []
delta2 = []
delta3 = []
delta4 = []
delta5 = []
A = []
for i in range(0, len(xi)-1):
    delta1.append(y[i+1] - y[i])
    print(delta1)
    if i == 0:
        delta.append(y[i+1] - y[i])
for i in range(0, len(delta1)-1):
    delta2.append(delta1[i + 1] - delta1[i])
    print(delta2)
    if i == 0:
        delta.append(delta1[i + 1] - delta1[i])
for i in range(0, len(delta2)-1):
    delta3.append(delta2[i + 1] - delta2[i])
    print(delta3)
    if i == 0:
        delta.append(delta2[i + 1] - delta2[i])
for i in range(0, len(delta3)-1):
    delta4.append(delta3[i + 1] - delta3[i])
    print(delta4)
    if i == 0:
        delta.append(delta3[i + 1] - delta3[i])
for i in range(0, len(delta4)-1):
    delta5.append(delta4[i + 1] - delta4[i])
    print(delta5)
    if i == 0:
        delta.append(delta4[i + 1] - delta4[i])
print(delta)
