N = int(input())

for i in range(1, N+1):
    for j in range(1, N+1):
        if i%2 != 0:
            if j%2 != 0:
                print(j, end='')
            else:
                print('  ', end='')
        else:
            if j%2 != 0:
                print('  ', end='')
            else:
                print(j, end='')
    print()