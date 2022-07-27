x_st = int(input('Input X start: '))
y_st = int(input('Input Y start: '))
len = int(input('Input side length of origin square(mm):'))
layers = int(input('Input number of squares: '))
gap = float(input('Input gap between squares(mm): '))
speed = input('Input speed(mm/min): ')
fname = input('Input file name: ')

file = open(fname + '.txt', 'w')

for i in range(int(layers)):
    file.write('G0   X' + str(x_st-i*gap)     + ' Y' + str(y_st-i*gap)     + ' Z' + str(0) + ' F' + speed + '\n')
    file.write('G1   X' + str(x_st-i*gap)     + ' Y' + str(y_st+len+i*gap) + ' Z' + str(0) + ' F' + speed + '\n')
    file.write('G1   X' + str(x_st+len+i*gap) + ' Y' + str(y_st+len+i*gap) + ' Z' + str(0) + ' F' + speed + '\n')
    file.write('G1   X' + str(x_st+len+i*gap) + ' Y' + str(y_st-i*gap)     + ' Z' + str(0) + ' F' + speed + '\n')
    file.write('G1   X' + str(x_st-i*gap)     + ' Y' + str(y_st-i*gap)     + ' Z' + str(0) + ' F' + speed + '\n')

file.close()