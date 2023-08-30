from collections import deque

# 入力受け取り
N, Q = map(int, input().split())

# 連結している頂点リスト
connect = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    # a→b, b→a が連結している
    connect[a].append(b)
    connect[b].append(a)


# 各頂点のカウンタ
counter = [0] * (N + 1)

for _ in range(Q):
    p, x = map(int, input().split())
    # pのcounterにxを加算
    counter[p] += x

que = deque()

# Start地点に1を指定
que.append(1)

# 訪問済みチェック
visited = [False] * (N + 1)
visited[1] = True

# queが空になるまで
while que:
    # queの左から取り出してnowに格納
    now = que.popleft()
    now_number = counter[now]
    for to in connect[now]:
        if visited[to] is False:
            counter[to] += now_number
            visited[to] = True
            que.append(to)

# 0以外のcounterを出力
print(*counter[1:])
