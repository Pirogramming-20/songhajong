import random

def turning_logic(a, player):
    global num
    global turn
    for i in range(a):
        num = num + 1
        print(f"{player} : {num}")
    turn = not turn

# 턴이 돌아가는 알고리즘 구성 => 매개변수로 하면 안되므로 global을 사용해 
# num(결과)과 turn(computer의 턴, 나의 턴을 boolen타입으로 나타냄)변수의 값을 바꿈
# a는 숫자를 몇번 말할것인지, player는 플레이어의 이름을 저장한 매개변수.

def turning(a, player):
    if player != 'computer':
        turning_logic(a, player)
    else:
        turning_logic(a, player)

def brGame(a):
    global turn
    if turn == True:
        turning(a, 'computer')
    else:
        turning(a, 'player')

#위는 그냥 보기편하게 함수로 바꿔 작성. 가장 최상단의 함수이름을 과제대로 'brGame'으로 명명

num = 0
turn = True

# 위에서 언급한것처럼 num은 결과, turn은 컴퓨터와 본인의 차례를 boolen값으로 스위칭함

while(True):

    if turn == False:
        a = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ')
    else:
        a = randum_num = random.randint(1,3)
    # 내턴이면 입력할 수 있도록, 컴퓨터의 차례라면 몇번 반복할 것인지 랜덤으로 생성
    try:
        int(a)
        it_is = True
    except ValueError:
        it_is = False
    # 입력한 받은 값(a)가 정수인지 판별 하는 코드. 
        
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
