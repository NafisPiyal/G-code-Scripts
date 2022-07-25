from math import sqrt

len = int(input('Input side length of hexagon(mm):'))
ext = int(input('Input amount of extrusion(mm): '))
layers = int(input('Input number of layers: '))
z_gap = float(input('Input Z gap(mm): '))
speed = input('Input speed(mm/min): ')

def getY(num):
    temp = .5 * sqrt(3) * num
    return temp

for i in range(int(layers)):
    print('G1   X' + str(len*.5)         + ' Y' + str(0)                     + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len*1.5+ext)    + ' Y' + str(0)                     + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len*1.5)        + ' Y' + str(0)                     + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2+ext*.5)   + ' Y' + str(getY(len + ext))       + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2)          + ' Y' + str(getY(len))             + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len*1.5-ext*.5) + ' Y' + str(getY(len)*2+getY(ext)) + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len*1.5)        + ' Y' + str(getY(len)*2)           + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len*.5-ext)     + ' Y' + str(getY(len)*2)           + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len*.5)         + ' Y' + str(getY(len)*2)           + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(-ext*.5)        + ' Y' + str(getY(len)-getY(ext))   + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(0)              + ' Y' + str(getY(len))             + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len*.5+ext*.5)  + ' Y' + str(-getY(ext))            + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len*.5)         + ' Y' + str(0)                     + ' Z' + str(i*z_gap) + ' F' + speed)

input("Press enter to exit")
    