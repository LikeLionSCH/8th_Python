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