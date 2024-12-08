
def operations(N, M):
    operations = 0
    while all(a % 2 == 0 for a in M):
        M = [a // 2 for a in M]       
        operations += 1               
    return operations
N = int(input())
M = list(map(int, input().split()))
print(operations(N, M))

#https://codeforces.com/group/MWSDmqGsZm/contest/219774/my
