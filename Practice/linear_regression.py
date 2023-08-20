def getLinearEquation(data:[tuple]):
    Exy = 0
    Ex = 0
    Ey = 0
    n = len(data)
    Ex2 = 0

    for x,y in data:
        Exy += x*y
        Ex += x
        Ey += y
        Ex2 += x**2

    up = Exy - (Ex*Ey)/n
    down = Ex2 - (Ex**2)/n

    m = up/down
    c = (Ey/n) - m*(Ex/n)

    print(Exy,
Ex ,
Ey ,
Ex2,m)

    return m,c

datasets = [
    (2,7),
    (3,3),
    (7,6),
    (8,10),
    (12,9),
    (13,11),
]

datasets2 = [
    (1,2),
    (2,4),
    (3,6),
    (4,8),
    (5,10),
    (6,12),
]

datasets3 = [
    (72,84),
    (50,63),
    (81,77),
    (74,78),
    (94,90),
    (86,75),
    (59,49),
    (83,79),
    (65,77),
    (33,52),
    (88,74),
    (81,90),
]

m,c = getLinearEquation(datasets3)
print(f"y = {m:.3f}x + {c:.3f}")