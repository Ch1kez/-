b = []
a = '0'
while a != '':
    # print(a)
    a = input()
    if a.endswith('@@@'):
        continue
    elif a.startswith('##'):
        b.append(a[2:])
    else:
        b.append(a)
for el in b:
    print(el)