n, m, start = map(int, input().split())
a=[]
for i in range(n+1):
    a.append([])
for j in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(n+1):
    a[i].sort()

check =[]
for i in range(n+1):
    check.append(False)

def dfs(a, check, now):
    if not check[now]:
        check[now] = True
    else:
        return
    print(now, end=' ')
    for k in a[now]:
        dfs(a, check, k)

dfs(a, check, start)
print()

check = []
for i in range(n+1):
    check.append(False)

def bfs(a, check, now):
    queue = []
    queue.append(now)
    # print(now, end=' ') #프린트 여기서 하는게 아님
    check[now] = True
    while queue:
        now = queue[0]
        print(now, end=' ')
        queue = queue[1:]
        for i in a[now]:
            if not check[i]:
                queue.append(i)
                check[i] = True


bfs(a, check, start)
