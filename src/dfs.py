# 深さ優先探索
# https://atcoder.jp/contests/abc213/tasks/abc213_d

# 再帰回数上限 再帰関数を使用するときは必ず最初に書く
import sys

sys.setrecursionlimit(10**6)

# 入力の受け取り
N = int(input())

# 道の情報格納リスト
connect = [[] for _ in range(N + 1)]

# 道の情報受取
for _ in range(N - 1):
    A, B = map(int, input().split())
    connect[A].append(B)
    connect[B].append(A)
    # connect[2] = [1, 4]ならば,1, 4が連結している

# 小さい順に回るためsort
for i in range(N + 1):
    connect[i].sort()

ans = []


# dfs(今いる町, 前にいた町)
def dfs(now: int, pre: int) -> None:
    ans.append(now)
    # to: 今いる町から行ける町
    for to in connect[now]:
        # 前にいた町と違っていたら
        if to != pre:
            dfs(to, now)
            # 戻ってきたら答えへ格納
            ans.append(now)


# 最初の町=1, 前にいた町=-1としてStart
dfs(1, -1)
# dfs(1, -1) now=1, pre=-1, to=2, ans=[1]
# stack dfs(1, -1)
# dfs(2, 1) now=2, pre=1, to=1, ans=[1,2]
# dfs(2, 1) now=2, pre=1, to=4, ans=[1,2]
# stack dfs(2, 1), dfs(1, -1)
# dfs(4, 2) now=4, pre=2, to=2, ans=[1,2,4]
# dfs(2, 1) now=2, pre=1, to=4, ans=[1,2,4,2]
# dfs(1, -1) now=1, pre=-1, to=2, ans=[1,2,4,2,1]
# dfs(1, -1) now=1, pre=-1, to=3, ans=[1,2,4,2,1]
# stack dfs(1, -1)
# dfs(3, 1) now=3, pre=1, to=1, ans=[1,2,4,2,1,3]
# dfs(1, -1) now=1, pre=-1, to=3, ans=[1,2,4,2,1,3,1]


print(*ans)
