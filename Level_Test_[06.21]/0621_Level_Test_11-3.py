N = int(input())

arr = [['' if x%2 != y%2 else str(x+1) for x in range(N)] for y in range(N)]

for el in arr:
    print(' '.join(el))