num_list = list(map(int, input("숫자를 입력하세요 >> ").split()))

max_num = max(num_list)
min_num = min(num_list)

for i in num_list:
    print(i, end='\t')

print()

for i in num_list:
    if i == max_num:
        print("최대값", end='\t')
    elif i == min_num:
        print("최소값", end='\t')
    else:
        print(end='\t')