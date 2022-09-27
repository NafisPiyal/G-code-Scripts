from math import sqrt

len = int(input('Input side length of triangle(mm): '))
tri = int(input('Input number of base triangles: '))
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
    print('G1   X' + str(len/2)           + ' Y' + str(-inp_ext)            + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len/2)           + ' Y' + str(0)                   + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(-inp_ext)        + ' Y' + str(0)                   + ' Z' + str(i*z_gap) + ' F' + speed)
    
    for j in range(tri-1):
        x = len*j
        print('G1   X' + str(x+0)                   + ' Y' + str(0)                 + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+ext/2)               + ' Y' + str(getY(ext))         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len/2)               + ' Y' + str(getY(len))         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len+inp_ext/2)       + ' Y' + str(-getY(inp_ext))    + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len)                 + ' Y' + str(0)                 + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+(len/2)-inp_ext)     + ' Y' + str(0)                 + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len/2)               + ' Y' + str(0)                 + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len/2)               + ' Y' + str(getY(len)+inp_ext) + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len/2)               + ' Y' + str(getY(len))         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+ext)                 + ' Y' + str(getY(len))         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len)                 + ' Y' + str(getY(len))         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len)                 + ' Y' + str(-inp_ext)          + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len)                 + ' Y' + str(0)                 + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+(len/2)-(inp_ext/2)) + ' Y' + str(getY(ext))         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len/2)               + ' Y' + str(getY(len))         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+(len*1.5)+inp_ext)   + ' Y' + str(getY(len))         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len*1.5)             + ' Y' + str(getY(len))         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len-inp_ext/2)       + ' Y' + str(-getY(inp_ext))    + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len)                 + ' Y' + str(0)                 + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len)                 + ' Y' + str(getY(len)+inp_ext) + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len)                 + ' Y' + str(getY(len))         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+(len*1.5)+inp_ext)   + ' Y' + str(getY(len))         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len*1.5)             + ' Y' + str(getY(len))         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len*1.5)             + ' Y' + str(-inp_ext)          + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len*1.5)             + ' Y' + str(0)                 + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(x+len-inp_ext)         + ' Y' + str(0)                 + ' Z' + str(i*z_gap) + ' F' + speed)
    
    print('G1   X' + str(x+len)   + ' Y' + str(0)    + ' Z' + str(i*z_gap) + ' F' + speed)
    x += len
    print('G1   X' + str(x+ext/2)           + ' Y' + str(getY(ext))         + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(x+len/2)           + ' Y' + str(getY(len))         + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(x+len+inp_ext/2)   + ' Y' + str(-getY(inp_ext))    + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(x+len)             + ' Y' + str(0)                 + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(x+(len/2)-inp_ext) + ' Y' + str(0)                 + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(x+len/2)           + ' Y' + str(0)                 + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(x+len/2)           + ' Y' + str(getY(len)+inp_ext) + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(x+len/2)           + ' Y' + str(getY(len))         + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(x+len+inp_ext/2)   + ' Y' + str(getY(-inp_ext))    + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(x+len)             + ' Y' + str(0)                 + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(-inp_ext)          + ' Y' + str(0)                 + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(0)                 + ' Y' + str(0)                 + ' Z' + str(i*z_gap) + ' F' + speed)    
                
input("Press enter to exit")

