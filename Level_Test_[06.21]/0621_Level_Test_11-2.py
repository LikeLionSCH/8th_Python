N = int(input())
print('\n'.join(''.join(str(i) if i%2 == j%2 else '  ' for i in range(1, N+1)) for j in range(1, N+1)))