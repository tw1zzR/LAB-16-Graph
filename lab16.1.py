import matplotlib.pyplot as mp; import math

x=[i for i in range(-3,6)]
y=[]

for elem in x:
    if elem != 0:
        value = 2 * math.sin(elem) + math.log2(abs(elem))
    else:
        value = 2 * math.sin(elem)
    y.append(value)

mp.plot(x,y, 'm--')
mp.title("15.1")
mp.xlabel("X-axis")
mp.ylabel("Y-asis:")
mp.savefig('page.svg')
mp.show()

print("Result has been written to 'page.svg'")