from random import randint,random

with open("data2.csv","w") as f:
    f.write("id,x,y\n")
    for i in range(20):
        # a = randint(0,100)
        # b = randint(a-10,a+10)
        # c = randint(0,100)

        # if i >= 15:
        #     clss = 'A'
        # else:
        #     clss = 'B'

        point = 25
        d = random() * 20
        x = randint(0,50)
        y = randint(d**2-x**2)

        f.write(f"{i+1},{a},{b}\n")