
num = 0
turn = True

while(True):

    a = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ')

    try:
        int(a)
        it_is = True
    except ValueError:
        it_is = False

    if(it_is == True):
        a = int(a)
        if(a == 1 or a == 2 or a == 3):
            if turn == True:
                for i in range(0, a):
                    num = num + 1
                    print(f"playerA : {num}")
                turn = not turn
            else:
                for i in range(0, a):
                    num = num + 1
                    print(f"playerB : {num}")
                turn = not turn
        else:
            print('1,2,3 중 하나를 입력하세요')
    else:
        print('정수를 입력하세요')

    