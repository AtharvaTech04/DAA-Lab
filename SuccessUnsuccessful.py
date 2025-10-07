import sys

n = 4
keys = [10, 20, 30, 40]
p = [0.1, 0.2, 0.4, 0.3]         
q = [0.05, 0.1, 0.05, 0.05, 0.1] 

e = [[0] * (n + 2) for _ in range(n + 2)]
w = [[0] * (n + 2) for _ in range(n + 2)]
root = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 2):
    e[i][i - 1] = q[i - 1]
    w[i][i - 1] = q[i - 1]

for length in range(1, n + 1):
    for i in range(1, n - length + 2):
        j = i + length - 1
        e[i][j] = sys.float_info.max
        w[i][j] = w[i][j - 1] + p[j - 1] + q[j]

        for r in range(i, j + 1):
            t = e[i][r - 1] + e[r + 1][j] + w[i][j]
            if t < e[i][j]:
                e[i][j] = t
                root[i][j] = r

print(f"Minimum expected cost of OBST: {e[1][n]:.4f}")
