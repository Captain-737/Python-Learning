x = int(input())
y = str(x)[1:]
if len(str(x)) == 5:
    print(int(str(x)[::-1]))
else:
    print(int(str(x)[0:1] + y[::-1]))