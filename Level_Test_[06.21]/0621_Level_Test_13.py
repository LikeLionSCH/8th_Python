title = '''
구구단 프로그램을 실행합니다.
1. 홀수 구구단
2. 짝수 구구단
3. 종료
'''

def gugudan1():
    for i in range(2, 10):
        if i%2 != 0:
            print(f'\n{i}단')
            for j in range(1, 10):
                print(f'{i} * {j} = {i*j}')

def gugudan2():
    for i in range(2, 10):
        if i%2 == 0:
            print(f'\n{i}단')
            for j in range(1, 10):
                print(f'{i} * {j} = {i*j}')

while True:
    print(title)
    num = int(input("숫자를 입력하세요: "))

    if num == 1:
        gugudan1()
    elif num == 2:
        gugudan2()
    elif num == 3:
        print("프로그램을 종료 합니다.")
        break
    else:
        print("잘못 입력하셨습니다. 1 ~ 3번 숫자를 입력하세요.")
        continue