str_ = ''
s_dif = set(input()).intersection(set(input()))
for el in s_dif:
    # print(el, type(el))
    str_ += el
print(str_)
# print(s_dif)