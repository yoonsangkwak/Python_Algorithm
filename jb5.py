def f_to_c(f):
    c = (f-32)*5/9
    return c


temp_list = [40, 15, 32, 64, -4, 11]
new_list = []
i = 0
while i < len(temp_list):
    # temp_list.insert(i,round(f_to_c(temp_list[i]),1))
    new_list.append(i)
    i += 1

print(new_list)
# print(temp_list)