# https://atcoder.jp/contests/abc231/tasks/abc231_c
import bisect

# 入力の受け取り
N, Q = map(int, input().split())
A = list(map(int, input().split()))

# Sorting A
A.sort()

for _ in range(Q):
    # 入力の受け取り
    x = int(input())

    # xがAの中で最小の要素以下である場合
    if x <= A[0]:
        print(N)
    # xがAの中で最大の要素より大きい場合
    elif A[N - 1] < x:
        print(0)
    # 二分探索
    else:
        right_bit = bisect.bisect_left(A, x)

        # 答え: (N - right_bit)人
        print(N - right_bit)
