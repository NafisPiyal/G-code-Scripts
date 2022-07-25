x_st = int(input('Input X start: '))
y_st = int(input('Input Y start: '))
x_len = int(input('Input length of specimen(mm):'))
y_count = input('Input number of lines: ')
y_gap = int(input('Input gap between lines(mm): '))
layers = input('Input number of layers: ')
speed = input('Input speed(mm/min): ')


if int(layers) == 1:
    for i in range(int(y_count)):
        if i % 2 == 0:
            print('G1   X' + str(0+x_st) + ' Y' + str(i*y_gap+y_st) + ' F' + speed) 
            print('G1   X' + str(x_len+x_st)  + ' Y' + str(i*y_gap+y_st) + ' F' + speed)
        else:
            print('G1   X' + str(x_len+x_st)  + ' Y' + str(i*y_gap+y_st) + ' F' + speed)
            print('G1   X' + str(0+x_st) + ' Y' + str(i*y_gap+y_st) + ' F' + speed) 
else:
    for j in range(int(layers)):
        for i in range(int(y_count)):
            if i % 2 == 0:
                print('G1   X' + str(0+x_st) + ' Y' + str(i*y_gap+y_st) + ' Z' + str(j) + ' F' + speed) 
                print('G1   X' + str(x_len+x_st)  + ' Y' + str(i*y_gap+y_st) + ' Z' + str(j) + ' F' + speed)
            else:
                print('G1   X' + str(x_len+x_st)  + ' Y' + str(i*y_gap+y_st) + ' Z' + str(j) + ' F' + speed)
                print('G1   X' + str(0+x_st) + ' Y' + str(i*y_gap+y_st) + ' Z' + str(j) + ' F' + speed)

input("Press enter to exit")

