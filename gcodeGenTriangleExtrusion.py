from math import sqrt

len = int(input('Input side length of triangle(mm):'))
inp_ext = int(input('Input amount of extrusion(mm): '))
layers = int(input('Input number of layers: '))
z_gap = float(input('Input Z gap(mm): '))
speed = input('Input speed(mm/min): ')

ext = len + inp_ext

def getY(num):
    temp = .5 * sqrt(3) * num
    return temp

for i in range(int(layers)):
    print('G1   X' + str(0)               + ' Y' + str(0)                   + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(ext/2)           + ' Y' + str(getY(ext))           + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len/2)           + ' Y' + str(getY(len))           + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len + inp_ext/2) + ' Y' + str(getY(len)-getY(ext)) + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len)             + ' Y' + str(0)                   + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(-inp_ext)        + ' Y' + str(0)                   + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(0)               + ' Y' + str(0)                   + ' Z' + str(i*z_gap) + ' F' + speed)

input("Press enter to exit")

