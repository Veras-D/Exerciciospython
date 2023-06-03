h1 = 3310.78; h2 = 2669.73; h3 = 2298.17; h4 = 417.5; h5 = 418.44; h6 = 762.52; h7 = 778.298
y = (h6 - h5) / (h2 - h5)
Wliq = 200 * 1000 * 3600
wt = h1 - h2 + (1 - y) * (h2 - h3)
qcond = (1 - y) * (h4 - h3)
wb = (1 - y) * (h4 - h5) + h6 - h7
qgv = h1 - h7
rend = (wt - abs(wb)) / qgv
m_fluxo = Wliq / (wt - abs(wb))
print(f"y = {y * 100}%")
print(f"wliq = {Wliq} Kj/h")
print(f"wt = {wt} Kj/Kg")
print(f"qcond = {qcond} Kj/Kg")
print(f"wb = {wb} Kj/Kg")
print(f"qgv = {qgv} Kj/Kg")
print(f"rend = {rend * 100}%")
print(f"Fluxo de massa = {m_fluxo} Kg/h")
print(f'mresf = {m_fluxo * y} Kg/h')
