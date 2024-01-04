
num = 0

while(True):

    a = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ')

    try:
        int(a)
        it_is = True
    except ValueError:
        it_is = False

    if(it_is == True):
        if(int(a) == 1 or int(a) == 2 or int(a) == 3):
            break
        else:
            print('1,2,3 중 하나를 입력하세요')
    else:
        print('정수를 입력하세요')

    