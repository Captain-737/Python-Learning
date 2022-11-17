text = str(input())
kop = (len(text) * 60) % 100
rub = (len(text) * 60) // 100
print(f'{rub} р. {kop} коп.')