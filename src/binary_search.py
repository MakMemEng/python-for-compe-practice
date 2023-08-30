# 二分探索Algorithm
# https://atcoder.jp/contests/abc231/tasks/abc231_c

# 入力の受け取り
N, Q = map(int, input().split())
A = list(map(int, input().split()))

# Aをsort
A.sort()

# Q回
for _i in range(Q):
    x = int(input())

    # xがAの中で最小の要素以下である場合
    if x <= A[0]:
        # N人
        print(N)
    elif A[N - 1] < x:
        print(0)
    # 二分探索
    else:
        left_bit = 0
        right_bit = N - 1
        # 1 < right_bit - left_bitの間
        while 1 < right_bit - 1:
            center_bit = (left_bit + right_bit) // 2
            # A[center_bit] < x (条件を満たさない場合)
            if A[center_bit] < x:
                left_bit = center_bit
            # x ≦ A[center_bit] (条件を満たす場合)
            else:
                right_bit = center_bit
        print(N - right_bit)
