n, k = int(input()), int(input())
sp = [i for i in range(1, n + 1)]
for i in range(len(sp)):
    while len(sp) > 1:
        i = (i + k - 1) % len(sp)
        sp.pop(i)
print(*sp)