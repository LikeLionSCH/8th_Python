name = ''

# CASE 1
participants1 = ['leo', 'kiki', 'eden']
completions1 = ['eden', 'kiki']

# CASE 2
participants2 = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completions2 = ['josipa', 'filipa', 'marina', 'nikola']

# CASE 3
participants3 = ['mislav', 'stanko', 'mislav', 'ana']
completions3 = ['stanko', 'ana', 'mislav']

dictionary = {}

# 리스트 -> 딕셔너리 변환
# key: 참가자 이름, value: 참가자 인원수
for participant in participants1:
    if participant not in dictionary:
        dictionary[participant] = 1 # 딕셔너리에 이름과 인원수 저장
    else:
        dictionary[participant] += 1 # 동명이인의 경우 인원수 +1명

# 참가자 목록에서 완주자 명단 제거
for completion in completions1:
    if completion not in dictionary:
        dictionary[completion] = 1
    else:
        dictionary[completion] -= 1 # 딕셔너리에서 완주자 이름에 대한 인원수 감소

for key, value in dictionary.items(): # 딕셔너리에서 key와 value 다 갖고와서
    if value > 0: # 남은 인원수가 1명이상인 경우
        name = key # 미완주자에 이름 등록

print(name)