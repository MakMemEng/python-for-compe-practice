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
        # 前にいた町を違っていたら
        if to != pre:
            dfs(to, now)
            # 戻ってきたら答えへ格納
            ans.append(now)


# 最初の町=1, 前にいた町=-1としてStart
dfs(1, -1)

print(*ans)
