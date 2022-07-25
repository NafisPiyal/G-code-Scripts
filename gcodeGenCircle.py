rad = int(input('Input radius of specimen(mm):'))
layers = input('Input number of layers: ')
z_gap = float(input('Input Z gap: '))
r_layers = input('Input radius layers: ')
r_gap = float(input('Input radius gap: '))
speed = input('Input speed(mm/min): ')



for j in range(int(layers)):
    if j % 2 == 0:
        for i in range(int(r_layers)):
            print('G1   X' + str(0+i*r_gap)     + ' Y' + str(rad)           + ' Z' + str(j*z_gap) + ' F' + speed)
            print('G2   X' + str(rad)           + ' Y' + str(rad*2-i*r_gap) + ' R' + str(rad-i*r_gap))
            print('G2   X' + str(rad*2-i*r_gap) + ' Y' + str(rad)           + ' R' + str(rad-i*r_gap))
            print('G2   X' + str(rad)           + ' Y' + str(0+i*r_gap)     + ' R' + str(rad-i*r_gap))
            print('G2   X' + str(0+i*r_gap)     + ' Y' + str(rad)           + ' R' + str(rad-i*r_gap))
    else:
        for i in range(int(r_layers)-1, -1, -1):
            print('G1   X' + str(0+i*r_gap)     + ' Y' + str(rad)           + ' Z' + str(j*z_gap) + ' F' + speed)
            print('G2   X' + str(rad)           + ' Y' + str(rad*2-i*r_gap) + ' R' + str(rad-i*r_gap))
            print('G2   X' + str(rad*2-i*r_gap) + ' Y' + str(rad)           + ' R' + str(rad-i*r_gap))
            print('G2   X' + str(rad)           + ' Y' + str(0+i*r_gap)     + ' R' + str(rad-i*r_gap))
            print('G2   X' + str(0+i*r_gap)     + ' Y' + str(rad)           + ' R' + str(rad-i*r_gap))
                

input("Press enter to exit")

