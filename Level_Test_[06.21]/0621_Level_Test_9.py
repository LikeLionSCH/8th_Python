str = input()
d = {}

for i in str:
    d[i] = 0

for i in str:
    d[i] += 1

maxValue = max(d.values())
result = [x for x in d.keys() if d[x] == maxValue]

'''
# 리스트 내포 안쓰면
result = []
for x in d.keys():
    if d[x] == maxValue:
        result.append(x)
'''

if len(result) > 1:
    print('?')
else:
    print(result[0])