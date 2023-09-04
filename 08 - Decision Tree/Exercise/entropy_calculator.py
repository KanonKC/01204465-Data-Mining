from math import log2

def entropy(clss):
    impurity = 0
    for c in clss:
        p = c / sum(clss)
        if p == 0:
            continue
        impurity += -p * log2(p)
    print(f"Impurity: {impurity:.3f}")
    return impurity

def entropyAll(classes):
    impurity = 0
    for clss in classes:
        impurity += sum(clss) / sum([sum(c) for c in classes]) * entropy(clss)
    return impurity

classes = []

while True:
    x = input()
    if x == "":
        break
    classes.append([int(i) for i in x.split()])

print(f"{entropyAll(classes):.3f}")