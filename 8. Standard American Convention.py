x = str(input())
num = ''

while len(x) > 3:
    while len(x) % 3 != 0:
        num += x[0]
        x = x[1:]
        if len(x) % 3 == 0:
            num += ','
    
    num = num + x[:3]
    if len(x) > 3:
        num += ','
    x = x[3:]

else:
    num += x

print(num)

"""
Самый короткий код:
num = int(input())
print(f"{num:,}")
"""