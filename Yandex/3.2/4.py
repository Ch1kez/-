
n = input()
m = input()
k_1 = []
k_2 = []
for i in range(int(n)):
    k_1.append(input())
# print(k_1)
for i in range(int(m)):
    k_2.append(input())
# print(k_2)
s_intersection = set(k_1).intersection(set(k_2))
# print(s_intersection)
if len(s_intersection) == 0:
    print('Таких нет')
else:
    print(len(s_intersection))