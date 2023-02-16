from math import *
import numpy as np

m1 = 2.4
m2 = 3.6
m3 = 4.8
R1_mod = 1.135
R2_mod = 0.822
R3_mod = 1.04
R1_ang = radians(113.4)
R2_ang = radians(48.8)
R3_ang = radians(251.4)
L1 = 0.854
L2 = 1.701
L3 = 2.396
Lb = 3.097
R1 = np.array([R1_mod * cos(R1_ang), R1_mod * sin(R1_ang)])
R2 = np.array([R2_mod * cos(R2_ang), R2_mod * sin(R2_ang)])
R3 = np.array([R3_mod * cos(R3_ang), R3_mod * sin(R3_ang)])
print(R1)
print(R2)
print(R3)
mRbx = (-m1 * R1[0] * L1 -m2 * R2[0] * L2 - m3 * R3[0] * L3) / Lb
mRby = (-m1 * R1[1] * L1 -m2 * R2[1] * L2 - m3 * R3[1] * L3) / Lb
print(mRbx, mRby)
mRb_mod = hypot(mRbx, mRby)
mRb_ang = degrees(atan2(mRby, mRbx))
print(mRb_mod, mRb_ang)
mRax = -m1 * R1[0] -m2 * R2[0] - m3 * R3[0] - mRbx
mRay = -m1 * R1[1] -m2 * R2[1] - m3 * R3[1] - mRby
print(mRax, mRay)
mRa_mod = hypot(mRax, mRay)
mRa_ang = degrees(atan2(mRay, mRay))
print(mRa_mod, mRa_ang)
