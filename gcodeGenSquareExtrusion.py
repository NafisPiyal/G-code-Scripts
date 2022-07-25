len = int(input('Input side length of square(mm):'))
ext = int(input('Input amount of extrusion(mm): '))
layers = int(input('Input number of layers: '))
z_gap = float(input('Input Z gap(mm): '))
speed = input('Input speed(mm/min): ')


for i in range(int(layers)):
    print('G1   X' + str(0)         + ' Y' + str(0)         + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(0)         + ' Y' + str(len + ext) + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(0)         + ' Y' + str(len)       + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len + ext) + ' Y' + str(len)       + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(len)       + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(-ext)      + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(0)         + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(-ext)      + ' Y' + str(0)         + ' Z' + str(i*z_gap) + ' F' + speed)
    print('G1   X' + str(0)         + ' Y' + str(0)         + ' Z' + str(i*z_gap) + ' F' + speed)
    
input("Press enter to exit")