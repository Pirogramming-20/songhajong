def brGame(a, player):
    for i in range(0, a):
        global num
        global turn
        num = num + 1
        print(f"player{player} : {num}")
    turn = not turn

def turning():
    global turn
    if turn == True:
        brGame(a, 'A')
    else:
        brGame(a, 'B')

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
            turning()

            if num >= 31:
                if turn == False:
                    print('playerB win!')
                else:
                    print('playerA win!')
                break
        else:
            print('1,2,3 중 하나를 입력하세요')
    else:
        print('정수를 입력하세요')
