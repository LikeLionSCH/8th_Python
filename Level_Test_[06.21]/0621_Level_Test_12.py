an = 1
bn = 2

for i in range(1, 5):
    for j in range(1, 10):
        for k in range(an, bn):
            print(f'{k} * {j} = {k*j}\t', end='')
        print()
    an = an + i
    bn = bn + i + 1
    print()