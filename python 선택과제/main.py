import random

def turning(a, player):
    global num
    global turn
    if player != 'computer':
        for i in range(a):
            num = num + 1
            print(f"{player} : {num}")
        turn = not turn
    else:
        for i in range(a):
            num = num + 1
            print(f"{player} : {num}")
        turn = not turn

def brGame(a):
    global turn
    if turn == True:
        turning(a, 'computer')
    else:
        turning(a, 'player')

num = 0
turn = True

while(True):
    
    if turn == False:
        a = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ')
    else:
        a = randum_num = random.randint(1,3)

    try:
        int(a)
        it_is = True
    except ValueError:
        it_is = False

    if(it_is == True):
        a = int(a)

        if(a == 1 or a == 2 or a == 3):
            brGame(a)

            if num >= 31:
                if turn == False:
                    print('player win!')
                else:
                    print('computer win!')
                break
        else:
            print('1,2,3 중 하나를 입력하세요')
    else:
        print('정수를 입력하세요')
