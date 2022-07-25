len = int(input('Input side length of square(mm):'))
ext = int(input('Input amount of extrusion(mm): '))
sqr = int(input('Input number of squares in each layer: '))
gap = float(input('Input gap between squares(mm): '))
layers = int(input('Input number of layers: '))
z_gap = float(input('Input Z gap(mm): '))
speed = input('Input speed(mm/min): ')


for i in range(layers):
    for j in range(sqr):
        print('G1   X' + str(0 + j*gap)         + ' Y' + str(0 + j*gap)         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(0 + j*gap)         + ' Y' + str(len + ext - j*gap) + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(0 + j*gap)         + ' Y' + str(len - j*gap)       + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(len + ext - j*gap) + ' Y' + str(len - j*gap)       + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(len - j*gap)       + ' Y' + str(len - j*gap)       + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(len - j*gap)       + ' Y' + str(-ext + j*gap)      + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(len - j*gap)       + ' Y' + str(0 + j*gap)         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(-ext + j*gap)      + ' Y' + str(0 + j*gap)         + ' Z' + str(i*z_gap) + ' F' + speed)
        print('G1   X' + str(0 + j*gap)         + ' Y' + str(0 + j*gap)         + ' Z' + str(i*z_gap) + ' F' + speed)
    
input("Press enter to exit")