name = input()
s = input()
a = []
for el in range(int(s)):
    sda = input()
    if len(sda) >= int(name):
        a.append(f'{sda[:int(name)]}...')
    else:
        a.append(f'{sda}')
for el in a:
    print(el)