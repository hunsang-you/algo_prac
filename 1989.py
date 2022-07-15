T = int(input())

for TC in range(1, T+1) :
    data = input()
    temp = ''
    for i in range(len(data)-1, -1, -1) :
        temp += data[i]
    if data == temp :
        print('#%d, %d' % (TC, 1))
    else :
        print('#%d, %d' % (TC, 0))