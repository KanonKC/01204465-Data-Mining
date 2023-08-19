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

    return m,c

datasets = [
    (2,7),
    (3,3),
    (7,6),
    (8,10),
    (12,9),
    (13,11),
]

m,c = getLinearEquation(datasets)
print(f"y = {m:.3f}x + {c:.3f}")