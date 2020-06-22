class Likelion0615:
    def first(self):
        print("나는 별이다...")
        num = int(input("얼마나 이동할까? "))

        i=0
        while i < num:
            print("\t"*i+"*")
            i = i + 1

    def second(self):
        for i in range(2, 10):
            print(f'{i} 단 :', end='')
            for j in range(1, 10):
                print(f' {i*j}', end='')
            print()

    def third(self):
        name = input("이름을 입력하세요: ")
        likelion = {'이남준':'010-6757-8402', '최민석':'010-3759-9397'}

        if name in likelion:
            print(name, "의 연락처는", likelion[name], '입니다.')
            print('삭제하겠습니다.')
            del likelion[name]
        else:
            print(name, "에 대한 정보가 없습니다. 등록합니다.")
            phone = input("전화번호를 입력하세요: ")
            likelion[name] = phone

        print()
        print("==현재 등록된 이름과 전화번호==")
        for name, phone in likelion.items():
            print(name, phone)

hw = Likelion0615()
hw.first()
hw.second()
hw.third()
