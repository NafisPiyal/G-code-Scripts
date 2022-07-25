x_st = int(input('Input X start: '))
y_st = int(input('Input Y start: '))
x_len = int(input('Input length of specimen(mm):'))
y_count = input('Input number of lines: ')
y_gap = int(input('Input gap between lines(mm): '))
layers = input('Input number of layers: ')
speed = input('Input speed(mm/min): ')
fname = input('Input file name: ')

file = open(fname + '.txt', 'w')

if int(layers) == 1:
    for i in range(int(y_count)):
        if i % 2 == 0:
            file.write('G1   X' + str(0+x_st) + ' Y' + str(i*y_gap+y_st) + ' F' + speed + '\n') 
            file.write('G1   X' + str(x_len+x_st)  + ' Y' + str(i*y_gap+y_st) + ' F' + speed + '\n')
        else:
            file.write('G1   X' + str(x_len+x_st)  + ' Y' + str(i*y_gap+y_st) + ' F' + speed + '\n')
            file.write('G1   X' + str(0+x_st) + ' Y' + str(i*y_gap+y_st) + ' F' + speed + '\n') 
else:
    for j in range(int(layers)):
        for i in range(int(y_count)):
            if i % 2 == 0:
                file.write('G1   X' + str(0+x_st) + ' Y' + str(i*y_gap+y_st) + ' Z' + str(j) + ' F' + speed + '\n') 
                file.write('G1   X' + str(x_len+x_st)  + ' Y' + str(i*y_gap+y_st) + ' Z' + str(j) + ' F' + speed + '\n')
            else:
                file.write('G1   X' + str(x_len+x_st)  + ' Y' + str(i*y_gap+y_st) + ' Z' + str(j) + ' F' + speed + '\n')
                file.write('G1   X' + str(0+x_st) + ' Y' + str(i*y_gap+y_st) + ' Z' + str(j) + ' F' + speed + '\n')

file.close()

